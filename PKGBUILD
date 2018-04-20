# Script generated with Bloom
pkgdesc="ROS - ROS device driver for Velodyne 3D LIDARs."
url='http://www.ros.org/wiki/velodyne_driver'

pkgname='ros-kinetic-velodyne-driver'
pkgver='1.3.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('libpcap'
'ros-kinetic-catkin'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-roslaunch'
'ros-kinetic-rostest'
'ros-kinetic-tf'
'ros-kinetic-velodyne-msgs'
)

depends=('libpcap'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-velodyne-msgs'
)

conflicts=()
replaces=()

_dir=velodyne_driver
source=()
md5sums=()

prepare() {
    cp -R $startdir/velodyne_driver $srcdir/velodyne_driver
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

