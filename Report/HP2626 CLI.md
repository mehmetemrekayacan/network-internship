Bu doküman HP 2626 switch’in 2007 donanım ve yazılım sürümü H.10.38 üzerinde test edilmiştir. Farklı firmware sürümlerinde bazı komutlar çalışmayabilir.

| Komut | Açıklama | Alt Komutlar / Parametreler |
| --- | --- | --- |
| boot | Cihazı yeniden başlatır. | system, &lt;cr&gt; |
| clear | Tablo/istatistikleri veya yetkili client key’lerini temizler. | arp, crypto, intrusion-flags, link-keepalive, logging, statistics |
| configure | Konfigürasyon moduna girer. | terminal, &lt;cr&gt; |
| copy | Dosyaları switch’e veya switch’ten kopyalar. | command-output, crash-data, crash-log, event-log, flash, running-config, startup-config, tftp, xmodem |
| debug | Debug loglamayı aç/kapat. | all, arp-protect, destination, dhcp-snooping, event, lldp |
| end | Manager Exec moduna geri döner. | &lt;cr&gt; |
| erase | Flash üzerindeki konfig veya image’i siler. | flash, startup-config |
| getMIB | Belirtilen MIB objelerini gösterir. | OBJECT-STR |
| kill | Başka session’ları sonlandırır. | &lt;1-4&gt;, &lt;cr&gt; |
| log | Log olaylarını gösterir. | \-a, -r, -m, -p, -w, -i, OPTION-STR, &lt;cr&gt; |
| page | Çıktı sayfalamasını aç/kapat. | &lt;cr&gt; |
| print | Komut çalıştırıp çıktıyı konsola yönlendirir. | COMMAND-STR |
| redo | Önceki komutu tekrar çalıştırır. | COMMAND-STR, NUMBER |
| reload | Switch’i sıcak reboot eder. | after, at, &lt;cr&gt; |
| repeat | Önceki komutları tekrarlar. | count, delay, NUMBER, &lt;cr&gt; |
| setMIB | MIB objesi değerini değiştirir. | OBJECT-STR |
| setup | Switch Setup ekranına girer (basic config). | default-logon, &lt;cr&gt; |
| telnet | Başka cihaza telnet ile bağlanır. | IP-ADDR |
| terminal | Terminal pencere boyutunu ayarlar. | length, width |
| update | Monitor ROM Console girer. | &lt;cr&gt; |
| walkMIB | Tüm belirtilen MIB objelerini listeler. | OBJECT-STR |
| write | Konfigürasyonu görüntüler veya kaydeder. | memory, terminal |
| enable | Manager Exec moduna geçer. | Yok |
| exit | Önceki moddan çıkış veya session sonlandırma. | &lt;cr&gt; |
| link-test | MAC adresine bağlantıyı test eder. | MAC-ADDR, repetitions, timeout, vlan |
| logout | Console/Telnet session’ını sonlandırır. | &lt;cr&gt; |
| menu | Konsol UI’yi menü sistemine değiştirir. | &lt;cr&gt; |
| ping | IP ping gönderir. | IP-ADDR, repetitions, timeout |
| show | Switch durum bilgilerini gösterir. | accounting, arp, arp-protect, authentication, banner, boot-history, cdp, config, console, cpu, crypto, debug, dhcp-relay, dhcp-snooping, fastboot, fault-finder, filter, flash, front-panel-security, gvrp, history, igmp, instrumentation, interfaces, ip, ip-lockdown, lacp, link-keepalive, lldp, lockout-mac, logging, loop-protect, mac-address, management, monitor, name, port-access, port-security, power-management, qos, radius, rmon, running-config, snmp-server, snmpv3, sntp, spanning-tree, stack, static-mac, system-information, tacacs, tech, telnet, terminal, time, timep, trunks, uptime, version, vlans |
| traceroute | Hedefe traceroute gönderir. | IP-ADDR |