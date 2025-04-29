# WSL QEMU-KVM with Windows Server 2016 VM Setup

<!-- This guide explains setting up QEMU/KVM virtualization inside WSL2 and installing a Windows Server 2016 VM -->

## Prerequisites
- Windows 11 with WSL2 enabled
- Ubuntu 20.04/22.04 WSL distribution installed
- Administrative privileges

## Steps

### 1. Update the package list
```bash
sudo apt-get update
```

### 2. Install virtualization packages
```bash
sudo apt install qemu qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virt-manager
sudo apt install x11-apps
```
<!-- x11-apps help with GUI applications like virt-manager -->

### 3. Try to enable libvirt services
```bash
sudo systemctl enable --now libvirtd
sudo systemctl enable --now virtlogd
```
<!-- These will fail because systemd is not active by default -->

### 4. Install Git
```bash
sudo apt install git
```

### 5. Clone and run the systemd enabling script
```bash
git clone https://github.com/DamionGans/ubuntu-wsl2-systemd-script.git
cd ubuntu-wsl2-systemd-script/
bash ubuntu-wsl2-systemd-script.sh
bash ubuntu-wsl2-systemd-script.sh --force
```
<!-- The --force option ensures the script applies even if WSL is already running -->

### 6. Shutdown the WSL instance
```bash
wsl --shutdown -d "<your-distribution-name>"
```
<!-- Replace <your-distribution-name> with your actual distro name, like Ubuntu-20.04 -->

### 7. Restart the WSL instance manually

### 8. Re-enable libvirt services after reboot
```bash
sudo systemctl enable --now libvirtd
sudo systemctl enable --now virtlogd
```

### 9. Launch the Virtual Machine Manager
```bash
virt-manager
```
<!-- Use Virt-Manager to create and manage your virtual machines -->

---

## Notes
- Ensure an X-server (like VcXsrv, X410) is running on Windows for GUI apps to display.
- If virt-manager can't find the hypervisor, manually connect to `qemu:///system`.
- During VM setup, mount the ISO of Windows Server 2016 located under `/mnt/<drive>/path/to/iso`.

---

## Troubleshooting
- If systemd still doesn't run after reboot, re-run the setup script with `--force`.
- If the GUI does not appear, check if the DISPLAY variable is set correctly (`echo $DISPLAY`).

---

## Credits
- Script by [DamionGans](https://github.com/DamionGans/ubuntu-wsl2-systemd-script)
