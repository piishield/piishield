# PIIShield

PIIShield is an open source library which helps organizations maintain compliance with privacy regulations such as HIPPA, GDPR, etc. Currently
it supports parsing audio, video, and text. 

After parsing the input, PIIShield will redact private (PII) data from the text/audio/video. For instance, an audio such as 

```
I am Johnny Appleseed, and I plant apple trees!
```

Would sound like 

```
I am <low bleep>, and I plant apple trees!
```

The transcript would appear like
3 
```
I am [Name], and I plant apple trees!
```

## Features

Beyond redaction in audio and transcripts of audio, PIIShield offers a number of key features. 

- Support for GDPR
    - These get redacted within the input and replaced with `[Name], [Location]`, etc.
- Underage detection (warnings displayed when used by underage individuals)
    - A `Warning` is displayed for communications detected to be by underage individuals.
    - If the input is of a medical nature, a call to action is displayed for reaching out to legal guardian.
- Risk analysis for employee and internal company data.
    - Input is analyzed for any risk detected to company secrets, internal strategies, or employee data.

## Technical details

This library/tool leverages [whisper_timestamped](https://github.com/linto-ai/whisper-timestamped) and [ffmpeg](https://ffmpeg.org/).
to transcribe and segment audio/video into timestamped words. The text input is passed into the text processing layer where redaction and analysis occurs. 

After redaction and processing, ffmpeg is leveraged to redact the given timestamps in the audio 

It was made for a very specific use case. If you think we can improve general usability via better commands and help docs, please create an Issue and/or Pull Request.

The way it works is by passing it a video file. Any video file supported by `ffmpeg` will work. It will then output an audio only file for you to bring into your video editor of choice.

## Prerequisites

Most of this library's documentation assumes `pip` and `pipenv` with python3 to be installed. You will also need ffmpeg.

- python3
- pip https://pypi.org/project/pip/
- pipenv https://pipenv.pypa.io/en/latest/#install-pipenv-today
- ffmpeg https://ffmpeg.org

No testing has been done without these requirements. If you would like to see docs for other tools/etc please create an issue or PR.

## Installation

### Using Pip

```
pip install git+https://github.com/cmgriffing/autobleep.git
```

### Using Pipenv
Clone the repo.

Use this to establish the pipfile-based python env:

```
pipenv shell
```
```
pipenv install
```

The `Locking...` step can take a while. If you would like to use the locked version of dependencies you can use:

```
pipenv install --ignore-pipfile
```



## License

Copyright 2023 Janesh Chhabra 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
