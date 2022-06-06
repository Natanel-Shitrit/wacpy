# <p align="center">`wacpy`<br/><br/>Unofficial WhatsApp Cloud API Wrapper<br/>(WIP)</p>

[![Downloads](https://static.pepy.tech/personalized-badge/wacpy?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pepy.tech/project/wacpy)
[![Supported Versions](https://img.shields.io/pypi/pyversions/wacpy.svg?color=green&label=Python%20Version)](https://pypi.org/project/wacpy)
[![License](https://img.shields.io/pypi/l/wacpy?color=green&label=License)](https://github.com/Natanel-Shitrit/wacpy/blob/master/LICENSE)
[![Version](https://img.shields.io/pypi/v/wacpy?color=green&label=Version)](https://pypi.org/project/wacpy/)

## 📚 About
`wacpy` aims to be a complete python wrapper for the WhatsApp Cloud API.

## ⚙ Usage
Currently, wacpy is only providing WhatsApp Cloud API objects.

### <ins>The 2 main objects are:</ins>
### 📃 Message: (`wacpy.types.message.Message`)
  
The Message object is used to craft messages.

<img src="https://user-images.githubusercontent.com/65548905/172053107-f8ac2dd7-2584-48ae-853a-79c6bb569e56.png" width="500" height="350">

### 🔔 Notification: (`wacpy.types.notification.Notification`)

The Notification object is the object that gets sent to your webhook.

<img src="https://user-images.githubusercontent.com/65548905/172053061-3c970f8f-dcea-4f09-a953-c1860008f05d.png" width="400" height="450">

###### Images taken from [Official WhatsApp Cloud API Refrence](https://developers.facebook.com/docs/whatsapp/cloud-api/reference)

All other sub-objects exist under this 2 types.

## 🖥 Examples
* A simple message:
```python
from wacpy.types.message import Message, message # You can also import `message` from `wacpy.types`

Message(
    to='{{WHATSAPP_PHONE_NUMBER}}',
    text=message.Text(
        body="This is a simple message!"
    )
)
```
![image](https://user-images.githubusercontent.com/65548905/172054613-8de8b9df-efac-4b08-83e6-80d5d6e48c15.png)

* An Image:
```python
from wacpy.types import Message, message # You can also import `message` from `wacpy.types`

Message(
    to='{{WHATSAPP_PHONE_NUMBER}}',
    type='image',
    image=message.Media(
        link='https://i.imgur.com/Zf5eagv.png',
        caption='Some cute cats'
    )
)
```
![image](https://user-images.githubusercontent.com/65548905/172058834-6c90ddd5-1b12-43bf-89bf-3880bbdec3b2.png)


* Interactive Button List
```python
from wacpy.types import Message, message # You can also import `message` from `wacpy.types`

Message(
    to='{{WHATSAPP_PHONE_NUMBER}}',
    type='interactive',
    interactive=message.Interactive(
        type='list',
        action=message.interactive.Action(
            button='List',
            sections=[
                message.interactive.Section(
                    title='First Section',
                    rows=[
                        message.interactive.section.Row(
                            id='first_row',
                            title='First Row',
                            description='This is the first row description',
                        ),
                        message.interactive.section.Row(
                            id='second_row',
                            title='Second Row',
                            description='This is the second row description',
                        )
                    ]
                ),
                message.interactive.Section(
                    title='Second Section',
                    rows=[
                        message.interactive.section.Row(
                            id='first_row',
                            title='First Row',
                            description='This is the first row description',
                        ),
                        message.interactive.section.Row(
                            id='second_row',
                            title='Second Row',
                            description='This is the second row description',
                        )
                    ]
                )
            ]
        ),
        body=message.interactive.Body('This is the body text')
    )
)
```
![image](https://user-images.githubusercontent.com/65548905/172060815-c2ca075d-a048-45f9-aceb-d6c4bc95c79f.png)
<img src="https://user-images.githubusercontent.com/65548905/172060725-fcca5615-ac24-4b9e-8487-36d977523198.png" width="300" height="450">
###### [Click here to see more examples]() (Soon!)
