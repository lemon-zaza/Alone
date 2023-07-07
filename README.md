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
