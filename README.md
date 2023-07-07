# Alone
Auto install PRITUNL Linux OS.

* Ubuntu  18.04, 20.04


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

https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-debian-11-243261243130246d443771547031794d72784e6b36656d4a326e49732e
