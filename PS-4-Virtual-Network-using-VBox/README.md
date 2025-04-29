# Create a Virtual Network in Oracle VirtualBox

This guide explains how to set up a **host-only virtual network** in VirtualBox so that multiple virtual machines (VMs) can communicate with each other privately.

## Prerequisites
- Oracle VM VirtualBox installed
- At least two virtual machines (e.g., Ubuntu Server, Kali Linux)

## Steps

### 1. Create a Host-Only Network
1. Open **VirtualBox**.
2. Go to the **File** menu → **Host Network Manager**.
3. Click **Create** to make a new host-only adapter.
4. (Optional) Edit the subnet if needed (e.g., change 192.168.56.1 to 192.168.100.1).
5. Enable the **DHCP Server**, and adjust IP ranges as required.
6. Click **Apply** and **Close**.

### 2. Configure Virtual Machines
For each VM:
1. Select the VM → Click **Settings** → Go to **Network**.
2. Disable **Adapter 1**.
3. Enable **Adapter 2**.
4. Set Adapter 2 to **Host-Only Adapter**.
5. Choose the newly created host-only adapter from the Name dropdown.

### 3. Start and Verify
1. Power on the VMs.
2. On each VM, open a terminal and run:

<!-- Prevent accidental formatting of code -->
```
ip addr show
```
<!-- Done -->

- Verify that each VM has received an IP address from the defined subnet range.

### 4. Test Connectivity
1. From one VM, ping the IP address of the other:

<!-- Prevent accidental formatting of code -->
```
ping [other_vm_ip_address] -c 5
```
<!-- Done -->

2. Successful replies confirm that the VMs are on the same network and can communicate.

## Notes
- **Host-Only Networking** ensures that VMs can talk to each other and the host machine but are isolated from the internet.
- Ensure firewall settings inside VMs are not blocking ICMP (ping) requests if you face issues.
