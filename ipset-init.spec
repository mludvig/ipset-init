Summary:	IP sets utility
Name:		ipset-init
Version:	1.0
Release:	0
License:	GPL
Group:		Applications/System
Source0:	ipset.init
Source1:	ipset-config
URL:		http://ipset.netfilter.org/
Requires:	ipset >= 6.0
BuildArch:	noarch

%description
IPset "init script" for automatic loading and saving existing ipset
tables.

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT/etc/rc.d/init.d/ipset
install -D %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/ipset-config
cat > $RPM_BUILD_ROOT/etc/sysconfig/ipset << __EOF__
## Use /usr/sbin/ipset tool to populate your ipset tables
## and then 'service ipset save' to save them to this file.
__EOF__

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add ipset
/sbin/chkconfig ipset on

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del %{pname}
fi

%files
%defattr(600,root,root,755)
%attr(755,root,root) /etc/rc.d/init.d/ipset
%config(noreplace) /etc/sysconfig/ipset*

