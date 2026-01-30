// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from tutorial_interfaces:msg/Controls.idl
// generated code does not contain a copyright notice
#include "tutorial_interfaces/msg/detail/controls__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
tutorial_interfaces__msg__Controls__init(tutorial_interfaces__msg__Controls * msg)
{
  if (!msg) {
    return false;
  }
  // target_sail_angle
  // target_sailflap_angle
  // target_backflap_angle
  // target_rudder_angle
  return true;
}

void
tutorial_interfaces__msg__Controls__fini(tutorial_interfaces__msg__Controls * msg)
{
  if (!msg) {
    return;
  }
  // target_sail_angle
  // target_sailflap_angle
  // target_backflap_angle
  // target_rudder_angle
}

bool
tutorial_interfaces__msg__Controls__are_equal(const tutorial_interfaces__msg__Controls * lhs, const tutorial_interfaces__msg__Controls * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // target_sail_angle
  if (lhs->target_sail_angle != rhs->target_sail_angle) {
    return false;
  }
  // target_sailflap_angle
  if (lhs->target_sailflap_angle != rhs->target_sailflap_angle) {
    return false;
  }
  // target_backflap_angle
  if (lhs->target_backflap_angle != rhs->target_backflap_angle) {
    return false;
  }
  // target_rudder_angle
  if (lhs->target_rudder_angle != rhs->target_rudder_angle) {
    return false;
  }
  return true;
}

bool
tutorial_interfaces__msg__Controls__copy(
  const tutorial_interfaces__msg__Controls * input,
  tutorial_interfaces__msg__Controls * output)
{
  if (!input || !output) {
    return false;
  }
  // target_sail_angle
  output->target_sail_angle = input->target_sail_angle;
  // target_sailflap_angle
  output->target_sailflap_angle = input->target_sailflap_angle;
  // target_backflap_angle
  output->target_backflap_angle = input->target_backflap_angle;
  // target_rudder_angle
  output->target_rudder_angle = input->target_rudder_angle;
  return true;
}

tutorial_interfaces__msg__Controls *
tutorial_interfaces__msg__Controls__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__Controls * msg = (tutorial_interfaces__msg__Controls *)allocator.allocate(sizeof(tutorial_interfaces__msg__Controls), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(tutorial_interfaces__msg__Controls));
  bool success = tutorial_interfaces__msg__Controls__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
tutorial_interfaces__msg__Controls__destroy(tutorial_interfaces__msg__Controls * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    tutorial_interfaces__msg__Controls__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
tutorial_interfaces__msg__Controls__Sequence__init(tutorial_interfaces__msg__Controls__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__Controls * data = NULL;

  if (size) {
    data = (tutorial_interfaces__msg__Controls *)allocator.zero_allocate(size, sizeof(tutorial_interfaces__msg__Controls), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = tutorial_interfaces__msg__Controls__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        tutorial_interfaces__msg__Controls__fini(&data[i - 1]);
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
tutorial_interfaces__msg__Controls__Sequence__fini(tutorial_interfaces__msg__Controls__Sequence * array)
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
      tutorial_interfaces__msg__Controls__fini(&array->data[i]);
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

tutorial_interfaces__msg__Controls__Sequence *
tutorial_interfaces__msg__Controls__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__Controls__Sequence * array = (tutorial_interfaces__msg__Controls__Sequence *)allocator.allocate(sizeof(tutorial_interfaces__msg__Controls__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = tutorial_interfaces__msg__Controls__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
tutorial_interfaces__msg__Controls__Sequence__destroy(tutorial_interfaces__msg__Controls__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    tutorial_interfaces__msg__Controls__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
tutorial_interfaces__msg__Controls__Sequence__are_equal(const tutorial_interfaces__msg__Controls__Sequence * lhs, const tutorial_interfaces__msg__Controls__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!tutorial_interfaces__msg__Controls__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
tutorial_interfaces__msg__Controls__Sequence__copy(
  const tutorial_interfaces__msg__Controls__Sequence * input,
  tutorial_interfaces__msg__Controls__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(tutorial_interfaces__msg__Controls);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    tutorial_interfaces__msg__Controls * data =
      (tutorial_interfaces__msg__Controls *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!tutorial_interfaces__msg__Controls__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          tutorial_interfaces__msg__Controls__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!tutorial_interfaces__msg__Controls__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
