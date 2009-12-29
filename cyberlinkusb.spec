# TODO:
# - make use from: http://linux.thaj.net63.net/cyberlinkusb/files/cyberlinkusb-init-script-20090215
# - find a way of runtime binding configuration
Summary:	CyberLink Remote Control
Name:		cyberlinkusb
Version:	20081207
Release:	0.1
License:	Free + GPL (for some parts of code)
Group:		Applications/Graphics
Source0:	http://linux.thaj.net63.net/cyberlinkusb/files/%{name}-%{version}.tar.bz2
# Source0-md5:	54c2279e38fa791a8159b3b204439497
URL:		http://linux.thaj.net63.net/cyberlinkusb/
BuildRequires:	libusb-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cyberlinkusb catches with libusb signals from a CyberLink remote control and
simulates key presses in X.

%prep
%setup -q

%build
%{__make} \
	COMPILER="%{__cxx}" \
	WARNINGS="-Wall -Wextra %{rpmcxxflags}"
	
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL NEWS README
%attr(4755,root,root) %{_bindir}/*
