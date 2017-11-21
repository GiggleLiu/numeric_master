Install CTQMC-Libarry

## Install ALPSCore
use anaconda environment with python 2.7
```bash
# $ conda install -c gimli pygimli
$ conda install doxygen
$ git clone https://github.com/ALPSCore/ALPSCore.git
$ cd ALPSCore
$ mkdir build
$ cd build
$ cmake ..
$ sudo make install
```

## Install Triqs
```bash
$ git clone https://github.com/TRIQS/triqs.git
$ cd triqs
$ mkdir build
$ cmake ..
```

## Install CTQMC
```bash
$ conda install eigen
$ git clone https://github.com/ALPSCore/CT-HYB.git
$ mkdir build
$ cd build
$ cmake\
$     -DALPSCore_DIR=/path/to/ALPSCore \
$     -DCMAKE_INSTALL_PREFIX=/path/to/install/dir \
$     -DCMAKE_CXX_COMPILER=mpic++ \
$    ../CT-HYB
$ make
$ make test
$ make install
```
