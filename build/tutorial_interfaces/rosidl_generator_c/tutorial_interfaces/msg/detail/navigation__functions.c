// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from tutorial_interfaces:msg/Navigation.idl
// generated code does not contain a copyright notice
#include "tutorial_interfaces/msg/detail/navigation__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
tutorial_interfaces__msg__Navigation__init(tutorial_interfaces__msg__Navigation * msg)
{
  if (!msg) {
    return false;
  }
  // waypoint_latitude
  // waypoint_longitude
  // tacking_waypoint_latitude
  // tacking_waypoint_longitude
  // target_heading
  return true;
}

void
tutorial_interfaces__msg__Navigation__fini(tutorial_interfaces__msg__Navigation * msg)
{
  if (!msg) {
    return;
  }
  // waypoint_latitude
  // waypoint_longitude
  // tacking_waypoint_latitude
  // tacking_waypoint_longitude
  // target_heading
}

bool
tutorial_interfaces__msg__Navigation__are_equal(const tutorial_interfaces__msg__Navigation * lhs, const tutorial_interfaces__msg__Navigation * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // waypoint_latitude
  if (lhs->waypoint_latitude != rhs->waypoint_latitude) {
    return false;
  }
  // waypoint_longitude
  if (lhs->waypoint_longitude != rhs->waypoint_longitude) {
    return false;
  }
  // tacking_waypoint_latitude
  if (lhs->tacking_waypoint_latitude != rhs->tacking_waypoint_latitude) {
    return false;
  }
  // tacking_waypoint_longitude
  if (lhs->tacking_waypoint_longitude != rhs->tacking_waypoint_longitude) {
    return false;
  }
  // target_heading
  if (lhs->target_heading != rhs->target_heading) {
    return false;
  }
  return true;
}

bool
tutorial_interfaces__msg__Navigation__copy(
  const tutorial_interfaces__msg__Navigation * input,
  tutorial_interfaces__msg__Navigation * output)
{
  if (!input || !output) {
    return false;
  }
  // waypoint_latitude
  output->waypoint_latitude = input->waypoint_latitude;
  // waypoint_longitude
  output->waypoint_longitude = input->waypoint_longitude;
  // tacking_waypoint_latitude
  output->tacking_waypoint_latitude = input->tacking_waypoint_latitude;
  // tacking_waypoint_longitude
  output->tacking_waypoint_longitude = input->tacking_waypoint_longitude;
  // target_heading
  output->target_heading = input->target_heading;
  return true;
}

tutorial_interfaces__msg__Navigation *
tutorial_interfaces__msg__Navigation__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__Navigation * msg = (tutorial_interfaces__msg__Navigation *)allocator.allocate(sizeof(tutorial_interfaces__msg__Navigation), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(tutorial_interfaces__msg__Navigation));
  bool success = tutorial_interfaces__msg__Navigation__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
tutorial_interfaces__msg__Navigation__destroy(tutorial_interfaces__msg__Navigation * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    tutorial_interfaces__msg__Navigation__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
tutorial_interfaces__msg__Navigation__Sequence__init(tutorial_interfaces__msg__Navigation__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__Navigation * data = NULL;

  if (size) {
    data = (tutorial_interfaces__msg__Navigation *)allocator.zero_allocate(size, sizeof(tutorial_interfaces__msg__Navigation), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = tutorial_interfaces__msg__Navigation__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        tutorial_interfaces__msg__Navigation__fini(&data[i - 1]);
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
tutorial_interfaces__msg__Navigation__Sequence__fini(tutorial_interfaces__msg__Navigation__Sequence * array)
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
      tutorial_interfaces__msg__Navigation__fini(&array->data[i]);
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

tutorial_interfaces__msg__Navigation__Sequence *
tutorial_interfaces__msg__Navigation__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  tutorial_interfaces__msg__Navigation__Sequence * array = (tutorial_interfaces__msg__Navigation__Sequence *)allocator.allocate(sizeof(tutorial_interfaces__msg__Navigation__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = tutorial_interfaces__msg__Navigation__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
tutorial_interfaces__msg__Navigation__Sequence__destroy(tutorial_interfaces__msg__Navigation__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    tutorial_interfaces__msg__Navigation__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
tutorial_interfaces__msg__Navigation__Sequence__are_equal(const tutorial_interfaces__msg__Navigation__Sequence * lhs, const tutorial_interfaces__msg__Navigation__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!tutorial_interfaces__msg__Navigation__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
tutorial_interfaces__msg__Navigation__Sequence__copy(
  const tutorial_interfaces__msg__Navigation__Sequence * input,
  tutorial_interfaces__msg__Navigation__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(tutorial_interfaces__msg__Navigation);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    tutorial_interfaces__msg__Navigation * data =
      (tutorial_interfaces__msg__Navigation *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!tutorial_interfaces__msg__Navigation__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          tutorial_interfaces__msg__Navigation__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!tutorial_interfaces__msg__Navigation__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
