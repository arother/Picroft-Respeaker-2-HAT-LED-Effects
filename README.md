[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=oksbwn_Picroft-Respeaker-2-HAT-LED-Effects&metric=alert_status)](https://sonarcloud.io/dashboard?id=oksbwn_Picroft-Respeaker-2-HAT-LED-Effects)  [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=oksbwn_Picroft-Respeaker-2-HAT-LED-Effects&metric=code_smells)](https://sonarcloud.io/dashboard?id=oksbwn_Picroft-Respeaker-2-HAT-LED-Effects)  [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=oksbwn_Picroft-Respeaker-2-HAT-LED-Effects&metric=ncloc)](https://sonarcloud.io/dashboard?id=oksbwn_Picroft-Respeaker-2-HAT-LED-Effects)
## Picroft Respeaker 2 HAT LED Effects 
>Python files to make LED effects on Respeaker 2 HAT from SeedStudio. Forked from [here](https://github.com/respeaker/mic_hat)

## Run as a service.
> Find out the path to `python` bin folder inside the virtual env., use command `echo $VIRTUAL_ENV`, in my case it is `/home/pi/mycroft-core/.venv/`

Create a file `pixels.service` inside `/etc/systemd/system/`

```shell
$ sudo touch /etc/systemd/system/pixels.service
$ sudo nano /etc/systemd/system/pixels.service
```

and paste the following contents, make sure to change the `Working Directory` and path.

```shell
[Unit]
Description=Respeaker HAT pixels service
After=multi-user.target

[Service]
Type=idle
WorkingDirectory=/home/pi/Picroft-Respeaker-2-HAT-LED-Effects
ExecStart=/home/pi/mycroft-core/.venv/bin/python pixels.py
Restart=always
[Install]
WantedBy=multi-user.target
```

Now you need to enable the service,

```
$ sudo systemctl daemon-reload
$ sudo systemctl start pixels
$ sudo systemctl enable pixels
```

