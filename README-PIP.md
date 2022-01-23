<p align="center">
    <h1 align="center"><b>Python Terminal Media Viewer</b></h1>
    <p align="center"><b>View images and videos without leaving the console</b></p>
	<h2 align="center"><a href="https://github.com/kal39/ptmv">More info on GitHub</a></h2>
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
