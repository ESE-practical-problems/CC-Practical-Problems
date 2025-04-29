# 🛰️ File Transfer Between Virtual Machines (VMs)

This guide explains multiple methods to transfer files between two Virtual Machines (VMs) using different approaches based on specific requirements.

<!-- TOC -->
## 📦 Methods

We will cover:
- [Method 1: Using SCP over Custom NAT Network](#method-1-using-scp-over-custom-nat-network)
- [Method 2: Using VirtualBox Shared Folder](#method-2-using-virtualbox-shared-folder)
- [Method 3: Using Shared Clipboard and Drag-and-Drop](#method-3-using-shared-clipboard-and-drag-and-drop)
- [Method 4: Using an Intermediate Drive (USB / ISO)](#method-4-using-an-intermediate-drive-usb--iso)
<!-- /TOC -->

---

## Method 1: Using SCP over Custom NAT Network

This method sets up a virtual network between VMs and transfers files using the `scp` (secure copy) command.

### Steps:

1. **Create a Custom NAT Network** in VirtualBox and attach it to both VMs.
2. **Find the VM IP addresses** using:

    ```bash
    ifconfig
    ```
   *(If `ifconfig` is missing, install net-tools:)*  
    ```bash
    sudo apt install net-tools
    ```

3. **Transfer file** from one VM to another using `scp`:

    ```bash
    scp transfer.txt receiver_username@receiver_ip:/home/receiver_username/
    ```

   Example:
    ```bash
    scp transfer.txt sentry@10.0.2.4:/home/sentry/
    ```

4. **Accept the fingerprint** when prompted.

📚 **Reference**: [File Transfer between Virtual Machines using SCP - YouTube](https://youtu.be/0MaS0nZCTZc)

---

## Method 2: Using VirtualBox Shared Folder

Share a common folder between VMs for seamless file synchronization.

### Steps:

1. **Create a shared folder** on the Host Machine:

    ```bash
    mkdir ~/vm_shared_folder
    ```

2. For each VM:
   - Go to **Settings → Shared Folders**.
   - Add the created folder.
   - Check:
     - ✅ Auto-mount
     - ✅ Make Permanent

3. **Access the shared folder**:
   - After rebooting, find it under `/media/sf_<foldername>/` or in the file explorer.

4. **Fix permissions** if needed:

    ```bash
    sudo adduser $USER vboxsf
    reboot
    ```
📚 **Reference**: [File Transfer between Virtual Machines using Shared folder - YouTube](https://www.youtube.com/watch?v=h_adwDledYM)
---

## Method 3: Using Shared Clipboard and Drag-and-Drop

Enable clipboard and file drag-and-drop functionality between VMs and host.

### Steps:

1. Open **VirtualBox Manager** → **Settings → General → Advanced** tab for your VM.

2. Set:
   - **Shared Clipboard**: `Bidirectional`
   - **Drag and Drop**: `Bidirectional`

3. Use **copy-paste** or **drag-and-drop** between VM and Host.

---

## Method 4: Using an Intermediate Drive (USB / ISO)

Transfer files using external media when network sharing is not preferred.

### Steps:

1. **Prepare storage**:
   - Use a physical **USB drive**  
   - Or create an **ISO file**:

    ```bash
    mkisofs -o transfer.iso /path/to/folder
    ```

2. **Attach** the USB or ISO to each VM:
   - For USB: Enable USB Controller → Add Device
   - For ISO: Attach it under Optical Drive

3. **Transfer files** manually inside the VM.

4. To manually mount an ISO (if needed):

    ```bash
    sudo mount /dev/cdrom /mnt
    ```

---

## 📋 Quick Comparison

<!-- prevent browser auto-render -->
<!-- markdown table -->

| Feature | SCP (NAT) | Shared Folder | Shared Clipboard/Drag-Drop | USB/ISO Drive |
|:---|:---|:---|:---|:---|
| Setup Complexity | Medium | Easy | Very Easy | Medium |
| Speed | Network-dependent | Fast (local disk) | Fast (small files) | Very fast (local I/O) |
| Best For | Remote/secure copy | Ongoing sharing | Quick one-time transfer | Offline/large file transfer |
| Internet Needed? | No | No | No | No |

---

## 🎯 Conclusion

This guide covered four effective methods for transferring files between Virtual Machines:

- **SCP**: Recommended for secure, network-based file transfer.
- **Shared Folder**: Ideal for continuous collaboration.
- **Clipboard/Drag-Drop**: Suitable for quick, small file transfers.
- **USB/ISO Drive**: Best for offline and large data transfers.

Choose the method based on your use case and environment setup.

---

## ⚡ Additional Notes

- **Guest Additions** must be installed for Shared Folder, Clipboard, and Drag-Drop functionality.
- For USB passthrough, ensure the **VirtualBox Extension Pack** is installed.

