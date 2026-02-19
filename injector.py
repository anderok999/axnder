import os
import subprocess
import time

class AxnderEngine:
    def __init__(self):
        self.found_devices = []
        self._prepare_environment()

    def _prepare_environment(self):
        """Libera el protocolo SSDP en Windows."""
        if os.name == 'nt':
            servicios = ["SSDPSRV", "upnphost"]
            for srv in servicios:
                subprocess.run(f'net stop {srv} /y', shell=True, capture_output=True)

    def _kill_port_9000(self):
        """Elimina procesos residuales para liberar el canal de datos."""
        if os.name == 'nt':
            try:
                # Mata cualquier instancia previa de nanodlna
                subprocess.run('taskkill /F /IM nanodlna.exe /T', shell=True, capture_output=True)
                time.sleep(0.5)
            except:
                pass

    def scan_network(self):
        from nanodlna import devices
        self.found_devices = devices.get_devices(timeout=7)
        return self.found_devices

    def inject_sequence(self, device_index, target_file):
        target = self.found_devices[device_index]
        location = target.get('location', '') if isinstance(target, dict) else getattr(target, 'location', '')
        intro_video = "intro_axnder.mp4"
        self._kill_port_9000()
        try:
            subprocess.Popen(f'nanodlna play "{intro_video}" --device "{location}"', shell=True)
            time.sleep(6.5) 
            self._kill_port_9000()
            subprocess.Popen(f'nanodlna play "{target_file}" --device "{location}"', shell=True)
            return True
        except:
            return False

    def inject_direct(self, device_index, target_file):
        target = self.found_devices[device_index]
        location = target.get('location', '') if isinstance(target, dict) else getattr(target, 'location', '')
        self._kill_port_9000()
        subprocess.Popen(f'nanodlna play "{target_file}" --device "{location}"', shell=True)
        return True

    def stop_all(self, device_index):
        target = self.found_devices[device_index]
        location = target.get('location', '') if isinstance(target, dict) else getattr(target, 'location', '')
        self._kill_port_9000()
        subprocess.run(f'nanodlna stop --device "{location}"', shell=True)