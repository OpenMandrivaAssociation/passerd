%define checkout ehabkost-passerd-dfda327

Name:          passerd
Summary:       A Twitter client that works as an IRC server
Version:       0.1.1
Release:       %mkrel 1
Source0:       %{checkout}.tar.gz
Source1:       passerd.initscript
URL:           http://passerd.raisama.net
License:       MIT
Group:         Networking/IRC
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: python-devel

Requires: python-daemon
Requires: python-twitty
Requires: python-twisted-words
Requires: python-sqlite
Requires: python-sqlalchemy
Requires: python-oauth

%description
Passerd is a IRC-Twitter gateway

%prep
%setup -q -n %{checkout}

%build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
mkdir -p %{buildroot}/%{_initrddir} %{buildroot}/%{_var}/lib/passerd
install %{SOURCE1} %{buildroot}/%{_initrddir}/%{name}

%post
echo -e "\n------------------------------------------------------------------------------------------"
echo -e "Please make sure to read the setup instructions at /usr/share/doc/passerd/USERGUIDE.markdown"
echo -e "before you start Passerd for the first time. It will guide you through the whole process."
echo -e "------------------------------------------------------------------------------------------\n"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/logo.txt COPYING CREDITS.markdown INSTALL.markdown NEWS.markdown README.markdown USERGUIDE.markdown
%{_initrddir}/%{name}
%{_var}/lib/%{name}
%{python_sitelib}/*
%{_bindir}/%{name}
