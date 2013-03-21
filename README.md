# Title

### Description.

---

#### SUBHEAD

* Item
* Item
* Item

---

#### INFO

Further documentation and examples can be found in [this project's wiki](https://github.com/registerguard/ghboiler/wiki).

---

#### DEMO

[![qr code](http://chart.apis.google.com/chart?cht=qr&chl=https://github.com/user/repo/&chs=240x240)](http://user.github.com/repo/demo/)

(Scan QR code with phone and/or click to [view the latest demo](http://user.github.com/repo/demo/).)

---

#### INSTALLATION

Install using [`pip`](http://www.pip-installer.org/):

```bash
$ sudo pip install -e git+https://github.com/user/repository.git#egg=XXXXXX
```

Add `'app_name',` to your `installed_apps` setting.

Put this in your URLs:

```python
(r'^foo/', include('app_name.urls')),
```

Run:

```bash
$ sudo service apache2 restart
```

... or:

```bash
$ touch apache/django.wsgi
```

... or whatever you need to do to reload things.

Lastly:

```bash
$ python manage.py syncdb
```

... and you're ready to go (maybe do another `touch`?)!

Enjoy your **Django App Name** app _today!_

---

#### CONTRIBUTING

**Submitting pull requests:**

1. Create a new branch, please don't work in master directly.
1. Add/write/modify code.
1. Test your code (includes cross-browser tests).
1. Fix stuff.
1. Repeat steps 2-4 until done.
1. Update the documentation to reflect any changes.
1. Push to your fork and submit a pull request.

---

#### SYNTAX

* In general, use a 4-space tab for primary indentation alignment and then spaces on top of that for detail alignment (unless it's Python, then it's 4 spaces per indent).
* No more than one assignment per var statement.
* Delimit strings with single-quotes ', not double-quotes ".
* Prefer if and else to "clever" uses of ? : conditional or ||, && logical operators.
* Always add newline at the end of files.
* When in doubt, follow the conventions you see used in the source already.
* Lorem ipsum dolor sit amet.
* ...

---

#### LEGAL

Copyright &copy; 2013 [First Last](http://site.com)/[Company Name](http://foo.com)

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the LICENSE file, or at:

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
