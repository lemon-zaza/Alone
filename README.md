# Alone
Auto install PRITUNL Linux OS.

* Ubuntu 20.4
```
wget -O install https://raw.githubusercontent.com/PiTOn-0/Alone/master/ubuntu20
bash install
```
* Ubuntu 18.4
```
wget -O install https://raw.githubusercontent.com/PiTOn-0/Alone/master/ubuntu18
bash install
```

## ufw ปฎิเสธขาเข้า / อณูญาติขาออก

เมื่อทุกอย่างเสร็จแล้ว เป็นสิ่งสุดท้าย

```
sudo ufw status verbose
```
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
```

https://www.cyberciti.biz/faq/ubuntu-22-04-lts-set-up-ufw-firewall-in-5-minutes/
