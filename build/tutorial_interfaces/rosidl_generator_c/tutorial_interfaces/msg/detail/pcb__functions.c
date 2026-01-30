// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from tutorial_interfaces:msg/PCB.idl
// generated code does not contain a copyright notice
#include "tutorial_interfaces/msg/detail/pcb__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
tutorial_interfaces__msg__PCB__init(tutorial_interfaces__msg__PCB * msg)
{
  if (!msg) {
    return false;
  }
  // wind_speed
  // wind_direction
  // roll
  // pitch
  // yaw
  // latitude
  // longitude
  // heading
  // sail_angle
  // sailflap_angle
  // backflap_angle
  // rudder_angle
  return true;
}

void
tutorial_interfaces__msg__PCB__fini(tutorial_interfaces__msg__PCB * msg)
{
  if (!msg) {
    return;
  }
  // wind_speed
  // wind_direction
  // roll
  // pitch
  // yaw
  // latitude
  // longitude
  // heading
  // sail_angle
  // sailflap_angle
  // backflap_angle
  // rudder_angle
}

bool
tutorial_interfaces__msg__PCB__are_equal(const tutorial_interfaces__msg__PCB * lhs, const tutorial_interfaces__msg__PCB * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // wind_speed
  if (lhs->wind_speed != rhs->wind_speed) {
    return false;
  }
  // wind_direction
  if (lhs->wind_direction != rhs->wind_direction) {
    return false;
  }
  // roll
  if (lhs->roll != rhs->roll) {
    return false;
  }
  // pitch
  if (lhs->pitch != rhs->pitch) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  // latitude
  if (lhs->latitude != rhs->latitude) {
    return false;
  }
  // longitude
  if (lhs->longitude != rhs->longitude) {
    return false;
  }
  // heading
  if (lhs->heading != rhs->heading) {
    return false;
  }
  // sail_angle
  if (lhs->sail_angle != rhs->sail_angle) {
    return false;
  }
  // sailflap_angle
  if (lhs->sailflap_angle != rhs->sailflap_angle) {
    return false;
  }
  // backflap_angle
  if (lhs->backflap_angle != rhs->backflap_angle) {
    return false;
  }
  // rudder_angle
  if (lhs->rudder_angle != rhs->rudder_angle) {
    return false;
  }
  return true;
}

bool
tutorial_interfaces__msg__PCB__copy(
  const tutorial_interfaces__msg__PCB * input,
  tutorial_interfaces__msg__PCB * output)
{
  if (!input || !output) {
    return false;
  }
  // wind_speed
  output->wind_speed = input->wind_speed;
  // wind_direction
  output->wind_direction = input->wind_direction;
  // roll
  output->roll = input->roll;
  // pitch
  output->pitch = input->pitch;
  // yaw
  output->yaw = input->yaw;
  // latitude
  output->latitude = input->latitude;
  // longitude
  output->longitude = input->longitude;
  // heading
  output->heading = input->heading;
  // sail_angle
  output->sail_angle = input->sail_angle;
  // sailflap_angle
  output->sailflap_angle = input->sailflap_angle;
  // backflap_angle
  output->backflap_angle = input->backflap_angle;
  // rudder_angle
  output->rudder_angle = input->rudder_angle;
  return true;
}

tutorial_interfaces__msg__PCB *
tutorial_interfaces__msg__PCB__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__PCB * msg = (tutorial_interfaces__msg__PCB *)allocator.allocate(sizeof(tutorial_interfaces__msg__PCB), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(tutorial_interfaces__msg__PCB));
  bool success = tutorial_interfaces__msg__PCB__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
tutorial_interfaces__msg__PCB__destroy(tutorial_interfaces__msg__PCB * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    tutorial_interfaces__msg__PCB__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
tutorial_interfaces__msg__PCB__Sequence__init(tutorial_interfaces__msg__PCB__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__PCB * data = NULL;

  if (size) {
    data = (tutorial_interfaces__msg__PCB *)allocator.zero_allocate(size, sizeof(tutorial_interfaces__msg__PCB), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = tutorial_interfaces__msg__PCB__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        tutorial_interfaces__msg__PCB__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
tutorial_interfaces__msg__PCB__Sequence__fini(tutorial_interfaces__msg__PCB__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      tutorial_interfaces__msg__PCB__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

tutorial_interfaces__msg__PCB__Sequence *
tutorial_interfaces__msg__PCB__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__PCB__Sequence * array = (tutorial_interfaces__msg__PCB__Sequence *)allocator.allocate(sizeof(tutorial_interfaces__msg__PCB__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = tutorial_interfaces__msg__PCB__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
tutorial_interfaces__msg__PCB__Sequence__destroy(tutorial_interfaces__msg__PCB__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    tutorial_interfaces__msg__PCB__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
tutorial_interfaces__msg__PCB__Sequence__are_equal(const tutorial_interfaces__msg__PCB__Sequence * lhs, const tutorial_interfaces__msg__PCB__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!tutorial_interfaces__msg__PCB__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
tutorial_interfaces__msg__PCB__Sequence__copy(
  const tutorial_interfaces__msg__PCB__Sequence * input,
  tutorial_interfaces__msg__PCB__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(tutorial_interfaces__msg__PCB);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    tutorial_interfaces__msg__PCB * data =
      (tutorial_interfaces__msg__PCB *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!tutorial_interfaces__msg__PCB__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          tutorial_interfaces__msg__PCB__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!tutorial_interfaces__msg__PCB__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
