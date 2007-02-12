Summary:	Active Spam Killer
Summary(pl.UTF-8):   Aktywny zabójca niechcianej poczty reklamowej
Name:		ask
Version:	2.5.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/sourceforge/a-s-k/%{name}-%{version}.tar.gz
# Source0-md5:	491ce48168d70365d7480a6d3c28f87d
URL:		http://www.paganini.net/ask/
Requires:	python
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

%description -l pl.UTF-8
Active Spam Killer (ASK) zabezpiecza skrzynkę pocztową przed
niechcianą pocztą reklamową poprzez potwierdzanie adresu nadawcy przed
właściwym dostarczeniem poczty. Potwierdzenie zachodzi poprzez
"wiadomość potwierdzającą", która jest wysyłana automatycznie do
wszystkich nieznanych użytkowników. Kiedy nadawca odpowie na tą
wiadomość (zwykła odpowiedź wystarczy), następne listy od tej osoby
będą dostarczane natychmiast. Można także podać (poprzez wyrażenie
regularne) adresy, które mają być od razu akceptowane, odrzucane (ze
stosowną odpowiedzią) lub ignorowane. Pakiet zawiera także narzędzie
do przeszukiwania starych skrzynek i generowania listy adresów do
automatycznego akceptowania.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_datadir}/ask/samples,%{_datadir}/ask/templates}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_libdir}/ask

install askfilter asksetup askversion.py utils/asksenders $RPM_BUILD_ROOT%{_bindir}
install askconfig.py asklock.py asklog.py askmail.py $RPM_BUILD_ROOT%{_libdir}/ask
install askmain.py askmessage.py askremote.py $RPM_BUILD_ROOT%{_libdir}/ask
install templates/* $RPM_BUILD_ROOT%{_datadir}/ask/templates
install docs/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog docs/ask_doc*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ask
%{_datadir}/ask
%{_mandir}/man1/*.1*
