# Script generated with Bloom
pkgdesc="ROS - Point cloud conversions for Velodyne 3D LIDARs."
url='http://ros.org/wiki/velodyne_pointcloud'

pkgname='ros-kinetic-velodyne-pointcloud'
pkgver='1.3.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-conversions'
'ros-kinetic-pcl-ros'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-roslaunch'
'ros-kinetic-roslib'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf2-ros'
'ros-kinetic-velodyne-driver'
'ros-kinetic-velodyne-msgs'
'yaml-cpp'
)

depends=('python2-yaml'
'ros-kinetic-angles'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-nodelet'
'ros-kinetic-pcl-ros'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-roslib'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-velodyne-driver'
'ros-kinetic-velodyne-laserscan'
'ros-kinetic-velodyne-msgs'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=velodyne_pointcloud
source=()
md5sums=()

prepare() {
    cp -R $startdir/velodyne_pointcloud $srcdir/velodyne_pointcloud
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

