Summary:	Active Spam Killer
Summary(pl):	Aktywny zabójca niechcianej poczty reklamowej
Name:		ask
Version:	2.4.1
Release:	1
License:	GPL
Group:		Applications/Mail
# Source0-md5:	91de4625710755e76d7f44e32d5fd763
Source0:	http://unc.dl.sourceforge.net/sourceforge/a-s-k/%{name}-%{version}.tar.gz
Requires:	python
URL:		http://www.paganini.net/ask/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Active Spam Killer (ASK) protects your email account against spam by
confirming the sender's email address before actual delivery takes
place. The confirmation happens by means of a "confirmation message"
that is automatically sent to all "unknown" users. Once the sender
replies to that message (a simple reply will do), future emails from
that person will be delivered immediately. You can also specify
(regexp) addresses to be immediately accepted, rejected (with a
nastygram) or ignored. The package also includes a utility to scan
your old mailboxes and generate a list of emails to be accepted
automatically.

%description -l pl
Active Spam Killer (ASK) zabezpiecza twoj± skrzynkê pocztow± przed
niechcian± poczt± reklamow±.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_datadir}/ask/samples,%{_datadir}/ask/templates}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_libdir}/ask

install ask.py asksetup.py askversion.py utils/asksenders.py $RPM_BUILD_ROOT%{_bindir}
install askconfig.py asklock.py asklog.py askmail.py $RPM_BUILD_ROOT%{_libdir}/ask
install askmain.py askmessage.py askremote.py $RPM_BUILD_ROOT%{_libdir}/ask
install samples/* $RPM_BUILD_ROOT%{_datadir}/ask/samples
install templates/* $RPM_BUILD_ROOT%{_datadir}/ask/templates
install docs/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
%{_libdir}/*
%doc docs/ask_doc*
