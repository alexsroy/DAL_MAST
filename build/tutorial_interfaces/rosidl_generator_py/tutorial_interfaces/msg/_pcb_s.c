// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from tutorial_interfaces:msg/PCB.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "tutorial_interfaces/msg/detail/pcb__struct.h"
#include "tutorial_interfaces/msg/detail/pcb__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool tutorial_interfaces__msg__pcb__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[33];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("tutorial_interfaces.msg._pcb.PCB", full_classname_dest, 32) == 0);
  }
  tutorial_interfaces__msg__PCB * ros_message = _ros_message;
  {  // wind_speed
    PyObject * field = PyObject_GetAttrString(_pymsg, "wind_speed");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->wind_speed = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // wind_direction
    PyObject * field = PyObject_GetAttrString(_pymsg, "wind_direction");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->wind_direction = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // roll
    PyObject * field = PyObject_GetAttrString(_pymsg, "roll");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->roll = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // pitch
    PyObject * field = PyObject_GetAttrString(_pymsg, "pitch");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->pitch = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // yaw
    PyObject * field = PyObject_GetAttrString(_pymsg, "yaw");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->yaw = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // latitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "latitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->latitude = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // longitude
    PyObject * field = PyObject_GetAttrString(_pymsg, "longitude");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->longitude = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // heading
    PyObject * field = PyObject_GetAttrString(_pymsg, "heading");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->heading = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // sail_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "sail_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->sail_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // sailflap_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "sailflap_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->sailflap_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // backflap_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "backflap_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->backflap_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // rudder_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "rudder_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->rudder_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * tutorial_interfaces__msg__pcb__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PCB */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("tutorial_interfaces.msg._pcb");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PCB");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  tutorial_interfaces__msg__PCB * ros_message = (tutorial_interfaces__msg__PCB *)raw_ros_message;
  {  // wind_speed
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->wind_speed);
    {
      int rc = PyObject_SetAttrString(_pymessage, "wind_speed", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // wind_direction
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->wind_direction);
    {
      int rc = PyObject_SetAttrString(_pymessage, "wind_direction", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // roll
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->roll);
    {
      int rc = PyObject_SetAttrString(_pymessage, "roll", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pitch
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->pitch);
    {
      int rc = PyObject_SetAttrString(_pymessage, "pitch", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // yaw
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->yaw);
    {
      int rc = PyObject_SetAttrString(_pymessage, "yaw", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // latitude
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->latitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "latitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // longitude
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->longitude);
    {
      int rc = PyObject_SetAttrString(_pymessage, "longitude", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // heading
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->heading);
    {
      int rc = PyObject_SetAttrString(_pymessage, "heading", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sail_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->sail_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sail_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // sailflap_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->sailflap_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "sailflap_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // backflap_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->backflap_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "backflap_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rudder_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->rudder_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rudder_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
