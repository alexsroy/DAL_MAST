// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from tutorial_interfaces:msg/Controls.idl
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
#include "tutorial_interfaces/msg/detail/controls__struct.h"
#include "tutorial_interfaces/msg/detail/controls__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool tutorial_interfaces__msg__controls__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[43];
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
    assert(strncmp("tutorial_interfaces.msg._controls.Controls", full_classname_dest, 42) == 0);
  }
  tutorial_interfaces__msg__Controls * ros_message = _ros_message;
  {  // target_sail_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_sail_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_sail_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // target_sailflap_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_sailflap_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_sailflap_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // target_backflap_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_backflap_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_backflap_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // target_rudder_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "target_rudder_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->target_rudder_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * tutorial_interfaces__msg__controls__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Controls */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("tutorial_interfaces.msg._controls");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Controls");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  tutorial_interfaces__msg__Controls * ros_message = (tutorial_interfaces__msg__Controls *)raw_ros_message;
  {  // target_sail_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_sail_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_sail_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // target_sailflap_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_sailflap_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_sailflap_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // target_backflap_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_backflap_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_backflap_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // target_rudder_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->target_rudder_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "target_rudder_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
