<!-- Title -->
# Install Linux Mint Cinnamon on VirtualBox (Linux Mint 20.3 Una)

<!-- Section: Minimum Requirements -->
## Minimum System Requirements
- RAM: Minimum 2 GB (Recommended 4 GB)
- Disk Space: Minimum 20 GB (Recommended 100 GB)
- CPU: At least 2 cores
- VirtualBox + Extension Pack installed
- Linux Mint 20.3 Cinnamon ISO file

---

<!-- Section: Installation Steps -->
## Installation Steps

<!-- Step 1: Download -->
### 1. Download Linux Mint ISO
- Go to: [https://linuxmint.com/](https://linuxmint.com/)
- Download **Linux Mint 20.3 Cinnamon** edition.
- Choose a nearby mirror to download faster.

<!-- Step 2: Virtual Machine Setup -->
### 2. Set Up Virtual Machine
- Open **VirtualBox** → Click **New**.
- **Name**: Linux Mint
- **Type**: Linux
- **Version**: Ubuntu (64-bit)
- **Memory Size**: 4096 MB (4 GB)
- **Hard Disk**: Create a virtual hard disk now
  - **File Type**: VDI (VirtualBox Disk Image)
  - **Storage**: Dynamically allocated
  - **Size**: 60 GB

<!-- Step 3: Configure VM -->
### 3. Configure VM Settings
- **System → Processor**: Allocate CPUs up to green limit.
- **Display → Screen**: Set Video Memory to 128 MB.
- **General → Advanced**: Set Shared Clipboard and Drag’n’Drop to "Bidirectional".
- **Storage**:
  - Select the empty optical drive.
  - Attach the downloaded Linux Mint ISO.

<!-- Step 4: Install Linux -->
### 4. Install Linux Mint
- Start the VM.
- Boot into "Start Linux Mint" (Live session).
- Double-click "**Install Linux Mint**" on desktop.
- Follow installer:
  - Language: English (default)
  - Keyboard: Default
  - Multimedia Codecs: Optional (skip if not needed)
  - Installation Type: Erase Disk (only affects virtual disk, safe)
  - Location: Set your region (example: New York)
  - User Setup: Create username and password.

<!-- Step 5: After Installation -->
### 5. Post-Installation
- After installation completes:
  - Shut down the VM.
  - Unmount the ISO (Settings → Storage → Remove Disk).

<!-- Step 6: Enable Features -->
### 6. Enable Full-Screen and Features
- Start the VM again.
- Go to **Devices → Insert Guest Additions CD Image**.
- Run the setup when prompted.
- Enter user password if required.
- Restart the VM after installation.
- Now you can:
  - Use full-screen mode.
  - Copy-paste and drag-drop between host and VM.

---

<!-- Section: Quick Tips -->
## Quick Tips
- If screen still doesn't resize properly, install Guest Additions again.
- Always shut down VM properly (avoid force close).
- Make sure you allocate enough CPU/RAM without entering the "red" zone.

---
