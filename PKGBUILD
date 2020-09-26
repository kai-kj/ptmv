# Maintainer: kal39 <kal390983@gmail.com>
pkgname=ptmv-git
pkgver=0.2.0
pkgrel=1
epoch=
pkgdesc="An utf-8/truecolor image and video viewer for the terminal."
arch=(x86_64 i686)
url="https://github.com/kal39/ptmv.git"
license=('MIT')
groups=()
depends=(youtube-dl)
makedepends=(git make  python3 python-pip)
checkdepends=()
optdepends=()
provides=(ptmv)
conflicts=(ptmv)
replaces=()
backup=()
options=()
install=
changelog=
source=("git+$url")
noextract=()
md5sums=('SKIP')
validpgpkeys=()

pkgvar() {
	cd "ptmv"
	printf "r%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "ptmv"
	sudo pip install pyinstaller opencv-python simpleaudio youtube-dl
	make build
}

package() {
	cd "ptmv"
	sudo make install
}
