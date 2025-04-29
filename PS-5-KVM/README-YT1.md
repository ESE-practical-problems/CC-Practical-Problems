# QEMU + KVM Installation Commands on Windows (via WSL 2)

<!-- Step 1 -->
## 🔹 Step 1: Install WSL and Set WSL 2 as Default
```bash
wsl --install
wsl --set-default-version 2
```
<!-- Explanation -->
- Installs Windows Subsystem for Linux (WSL) and sets version 2 as default.

---

<!-- Step 2 -->
## 🔹 Step 2: Update and Upgrade Packages inside WSL
```bash
sudo apt update && sudo apt upgrade -y
```
<!-- Explanation -->
- Refreshes package lists and updates installed software.

---

<!-- Step 3 -->
## 🔹 Step 3: Install QEMU, KVM, and Supporting Packages
```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils -y
```
<!-- Explanation -->
- Installs virtualization packages required for QEMU and KVM.

---

<!-- Step 4 -->
## 🔹 Step 4: Add Your User to the KVM Group
```bash
sudo usermod -aG kvm $USER
```
<!-- Explanation -->
- Grants your user permission to access KVM for hardware acceleration.

---

<!-- Step 5 -->
## 🔹 Step 5: Restart WSL
```bash
wsl --shutdown
```
<!-- Explanation -->
- Shuts down WSL to apply group membership changes.

---

<!-- Step 6 -->
## 🔹 Step 6: Create a Virtual Disk Image (30GB)
```bash
qemu-img create -f qcow2 ubuntu.qcow2 30G
```
<!-- Explanation -->
- Creates a 30GB `.qcow2` virtual hard disk for the Ubuntu installation.

---

<!-- Step 7 -->
## 🔹 Step 7: Launch and Install Ubuntu via QEMU
```bash
qemu-system-x86_64 -accel kvm -vga virtio -m 8G -smp 4 -drive file=ubuntu.qcow2,format=qcow2 -cdrom /mnt/path-to-ubuntu-iso -boot d
```
<!-- Explanation -->
- Launches the QEMU VM with:
  - KVM acceleration
  - Virtio VGA driver for better graphics
  - 8GB RAM, 4 CPU cores
  - Ubuntu ISO mounted for installation

---
