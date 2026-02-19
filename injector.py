import os
import subprocess
import time

class AxnderEngine:
    def __init__(self):
        self.found_devices = []

    def _kill_port_9000(self):
        """Busca y destruye cualquier proceso usando el puerto 9000 para evitar Error 10048"""
        if os.name == 'nt':
            try:
                # Busca el PID que está escuchando en el puerto 9000
                cmd = 'netstat -ano | findstr :9000'
                result = subprocess.check_output(cmd, shell=True).decode()
                for line in result.splitlines():
                    if "LISTENING" in line:
                        pid = line.strip().split()[-1]
                        subprocess.run(f'taskkill /F /PID {pid}', shell=True, capture_output=True)
                        print(f"[*] CANAL LIBERADO (PID {pid})")
                time.sleep(0.8)
            except:
                pass # El puerto ya está libre

    def scan_network(self):
        from nanodlna import devices
        self.found_devices = devices.get_devices(timeout=5)
        return self.found_devices

    def inject_sequence(self, device_index, target_file):
        """MODO SHOW: Intro de terminal + Archivo final"""
        target = self.found_devices[device_index]
        location = target.get('location', '') if isinstance(target, dict) else getattr(target, 'location', '')
        intro_video = "intro_axnder.mp4"

        self._kill_port_9000()

        try:
            print(f"\n[*] INICIANDO SECUENCIA COMPLETA EN: {location}")
            # FASE 1: Intro
            subprocess.Popen(f'nanodlna play "{intro_video}" --device "{location}"', shell=True)
            
            # Tiempo de espera de tu intro (ajustado a 6.5s)
            time.sleep(6.5) 
            
            # FASE 2: Purga y Cambio
            self._kill_port_9000()
            
            print(f"[+] ACCESO CONCEDIDO. PROYECTANDO PAYLOAD: {target_file}")
            subprocess.Popen(f'nanodlna play "{target_file}" --device "{location}"', shell=True)
            return True
        except Exception as e:
            print(f"[-] Error en secuencia: {e}")
            return False

    def inject_direct(self, device_index, target_file):
        """MODO NINJA: Inyección inmediata sin intro (para Ghost Write)"""
        target = self.found_devices[device_index]
        location = target.get('location', '') if isinstance(target, dict) else getattr(target, 'location', '')
        
        self._kill_port_9000()
        
        try:
            print(f"\n[*] EJECUTANDO INYECCIÓN DIRECTA EN: {location}")
            subprocess.Popen(f'nanodlna play "{target_file}" --device "{location}"', shell=True)
            return True
        except Exception as e:
            print(f"[-] Error en inyección directa: {e}")
            return False

    def stop_all(self, device_index):
        target = self.found_devices[device_index]
        location = target.get('location', '') if isinstance(target, dict) else getattr(target, 'location', '')
        self._kill_port_9000()
        subprocess.run(f'nanodlna stop --device "{location}"', shell=True)