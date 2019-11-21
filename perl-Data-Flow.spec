#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Flow
Version  : 1.02
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/I/IL/ILYAZ/modules/Data-Flow-1.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IL/ILYAZ/modules/Data-Flow-1.02.tar.gz
Source1  : http://cdn-fastly.deb.debian.org/debian/pool/main/libd/libdata-flow-perl/libdata-flow-perl_1.02-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Data-Flow-license = %{version}-%{release}
Requires: perl-Data-Flow-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
No detailed description available

%package dev
Summary: dev components for the perl-Data-Flow package.
Group: Development
Provides: perl-Data-Flow-devel = %{version}-%{release}
Requires: perl-Data-Flow = %{version}-%{release}

%description dev
dev components for the perl-Data-Flow package.


%package license
Summary: license components for the perl-Data-Flow package.
Group: Default

%description license
license components for the perl-Data-Flow package.


%package perl
Summary: perl components for the perl-Data-Flow package.
Group: Default
Requires: perl-Data-Flow = %{version}-%{release}

%description perl
perl components for the perl-Data-Flow package.


%prep
%setup -q -n Data-Flow-1.02
cd %{_builddir}
tar xf %{_sourcedir}/libdata-flow-perl_1.02-2.debian.tar.xz
cd %{_builddir}/Data-Flow-1.02
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Flow-1.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Flow
cp %{_builddir}/Data-Flow-1.02/deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Flow/6e634e2c798ecc82d11faca758a06863d490acfa
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Flow.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Flow/6e634e2c798ecc82d11faca758a06863d490acfa

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Data/Flow.pm
/usr/lib/perl5/vendor_perl/5.28.2/auto/Data/Flow/autosplit.ix
