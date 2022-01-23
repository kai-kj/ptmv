<p align="center">
    <h1 align="center"><b>Python Terminal Media Viewer</b></h1>
    <p align="center"><b>View images and videos without leaving the console</b></p>
    <p align="center">
    <img src="https://img.shields.io/github/license/kal39/ptmv">
    <img src="https://img.shields.io/github/languages/top/kal39/ptmv">
    <img src="https://img.shields.io/github/issues/kal39/ptmv">
    </p>
</p>


----

### Features

* View **images** form any terminal
* Watch **videos** from any terminal
* Watch **youtube** videos from any terminal (`-y`, `--youtube`)
* Play videos at **any fps** (`--fps`) with sound
* **Resize** images / videos (`--width`, `--height`)
* Easy to use

----

### Examples

**Viewing an image**

<img src="https://github.com/kal39/ptmv/blob/master/assets/image_demo.gif?raw=true" width="80%">

**Watching a video**

<img src="https://github.com/kal39/ptmv/blob/master/assets/video_demo.gif?raw=true" width="80%">

----

### Requirements

* A terminal that supports **truecolor** ([list](https://gist.github.com/XVilka/8346728)) and **utf-8** (most terminals should support utf-8).

----

### Usage

```shell
ptmv FILE [OPTIONS]
```

* **Required arguments**  

    * `FILE`

        File to display/play or youtube url

* **Optional arguments**  

  * `-y`. `--youtube` 
    View youtube videos

  * `--height` 
    Set height (setting both `width` and `height` will ignore original aspect ratio)

  * `--width` 
    Set width (setting both `width` and `height` will ignore original aspect ratio)

  * `--start-time`
    
    Set start position for video.

  * `-f`, `--fps` 
    Set fps (default 15 fps)

  * `-m`, `--mute` 
    Mute audio

  * `-h`, `--help ` 
    Display help

----

### Installation

```shell
pip install ptmv
```

----

### Contributing

Any contributions are greatly appreciated.

----

**kal39**(https://github.com/kal39) - kaikitagawajones@gmail.com
Distributed under the MIT license. See `LICENSE` for more information.
