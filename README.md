<p align="center">
	<h1 align="center"><b>Py Terminal Media Viewer</b></h1>
	<p align="center"><b>View images and videos without leaving the console</b></p>
	<p align="center">
	<img src="https://img.shields.io/github/license/kal39/ptmv">
	<img src="https://img.shields.io/github/languages/top/kal39/ptmv">
	<img src="https://img.shields.io/github/issues/kal39/ptmv">
	<img src="https://img.shields.io/github/v/release/kal39/ptmv?sort=semver">
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

<img src="https://github.com/kal39/TerminalMediaViewer/blob/master/assets/iGif.gif?raw=true" width="80%">

**Watching a video**

<img src="https://github.com/kal39/TerminalMediaViewer/blob/master/assets/vGif.gif?raw=true" width="80%">

----

### Requirements

* A terminal that supports **truecolor** ([list](https://gist.github.com/XVilka/8346728)) and **utf-8** (most terminals should support utf-8).

----

### Usage

**ptmv `FILE` `[OPTIONS]`**

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
  	
  * `-v`, `--volume`   
  	Set audio volume (0 ~ 1)
  	
  * `-i`, `--no-info`   
  	Disable progress bar for videos
  	
  * `-h`, `--help `  
  	Display help

----

### Installation

* **Using pip** ([PyPI](https://pypi.org/project/ptmv/))

  ```
  pip install ptmv
  ```

* **From source - binary**

  1. Install dependencies:

     ```
     pip install pyinstaller opencv-python simpleaudio youtube-dl
     ```
     **Note:** If `simpleaudio` fails to install, install it's dependency `libsound2-dev` first.   
     For example, with `apt`: `apt install libsound2-dev`

  2. Install:

     ```
     make build
     make install
     ```
* **From the AUR**
  ```
  git clone https://aur.archlinux.org/ptmv-git.git
  cd ptmv-git
  makepkg -si
  ```
  or
  ```
  yay ptmv-git
  ```
----

### Releases

----

### Contributing
Any contributions are greatly appreciated.

----

**kal39**(https://github.com/kal39) - kal390983@gmail.com  
Distributed under the MIT license. See `LICENSE` for more information.
