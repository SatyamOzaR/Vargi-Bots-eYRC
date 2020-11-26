#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/satyam/catkin_ws/src/vb_simulation_pkgs/gazebo_ros_pkgs/gazebo_plugins"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/satyam/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/satyam/catkin_ws/install/lib/python2.7/dist-packages:/home/satyam/catkin_ws/build/gazebo_plugins/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/satyam/catkin_ws/build/gazebo_plugins" \
    "/usr/bin/python2" \
    "/home/satyam/catkin_ws/src/vb_simulation_pkgs/gazebo_ros_pkgs/gazebo_plugins/setup.py" \
     \
    build --build-base "/home/satyam/catkin_ws/build/gazebo_plugins" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/satyam/catkin_ws/install" --install-scripts="/home/satyam/catkin_ws/install/bin"
