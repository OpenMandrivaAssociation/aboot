Summary: A bootloader which can be started from the SRM console
Name: aboot
%define aboot_version 0.9b
Version: %{aboot_version}
Release: %mkrel 3
ExclusiveArch: alpha
License: GPL
Group: System/Kernel and hardware
URL: http://www.sf.net/projects/aboot
Source: aboot-%version.tar.bz2
Patch0: aboot-0.7-cnf-config-file.patch
Patch1: aboot-0.7a-optflags.patch
Requires: common-licenses
Provides: bootloader
BuildRequires: kernel-source

%description
The aboot program is the preferred way of booting Linux when using SRM
firmware (the firmware normally used to boot an DEC UNIX). Aboot supports
the creation of bootable block devices and contains a program which can
load Linux kernels from a filesystem which is bootable by SRM.  Aboot
also supports direct booting from various filesystems (ext2, ISO9660,
UFS), booting of executable object files (ELF and ECOFF), booting of
compressed kernels, network booting (using bootp), partition tables in
DEC UNIX format, and interactive booting and default configurations for
SRM consoles that cannot pass long option strings.

If you are installing Mandriva Linux on an Alpha, you'll need to install
the aboot package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make MDK_OPT_FLAGS="$RPM_OPT_FLAGS" kversion=`uname -r`

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
chmod go= $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
%makeinstall root=$RPM_BUILD_ROOT bindir=$RPM_BUILD_ROOT/sbin
cp -p sdisklabel/swriteboot.8 tools/e2writeboot.8 $RPM_BUILD_ROOT%{_mandir}/man8

mv -f sdisklabel/README sdisklabel/README-sdisklabel || true

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc INSTALL README ChangeLog TODO aboot.conf sdisklabel/README-sdisklabel
%attr(644, root, root) /boot/bootlx
/sbin/abootconf
/sbin/e2writeboot
/sbin/isomarkboot
/sbin/swriteboot
%{_mandir}/man*/*

