# doorbell-push
Simple RPi python service for sending doorbell push notifications

I knocked this together so I could receive doorbell push events on my phone. The client app was activated by the push events and triggered a notification and a ping.

The doorbell is wired to GPIO pin 25 and a debounce time of 10 secs ensured we only got notified once for a push. The push notifications are sent by [Google Cloud Messaging](https://developers.google.com/cloud-messaging/gcm) (you need a free account and an API key).

I had bigger things in mind that I never got around to. I intended to add a camera action to take a picture of the visitor and send a link to the phone, but never got round to buying the camera. If anyone considers trying this please get in touch!
