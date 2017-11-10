Name:           ros-kinetic-velodyne-pointcloud
Version:        1.3.0
Release:        0%{?dist}
Summary:        ROS velodyne_pointcloud package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/velodyne_pointcloud
Source0:        %{name}-%{version}.tar.gz

Requires:       PyYAML
Requires:       ros-kinetic-angles
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-pcl-ros
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-velodyne-driver
Requires:       ros-kinetic-velodyne-laserscan
Requires:       ros-kinetic-velodyne-msgs
Requires:       yaml-cpp-devel
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-nodelet
BuildRequires:  ros-kinetic-pcl-conversions
BuildRequires:  ros-kinetic-pcl-ros
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf2-ros
BuildRequires:  ros-kinetic-velodyne-driver
BuildRequires:  ros-kinetic-velodyne-msgs
BuildRequires:  yaml-cpp-devel

%description
Point cloud conversions for Velodyne 3D LIDARs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Nov 10 2017 Josh Whitley <jwhitley@autonomoustuff.com> - 1.3.0-0
- Autogenerated by Bloom

