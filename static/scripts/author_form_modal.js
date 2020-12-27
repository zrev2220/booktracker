"use strict";

/**
 * Submit handler for add author form; makes an AJAX request to add an author.
 *
 * Returns a Promise that resolves when the request completes. If errors occurred but the response code was still 200,
 * resolves anyway--the caller is responsible for checking the response body for error messages.
 *
 * On success, adds the author to the top of the author select box and scrolls
 * the new option into view.
 * @param e {Event} Add author form's submit event.
 * @param $modal {jQuery} jQuery of the modal containing the submitted form.
 * @param isEditing {boolean} Flag indicating if the submission should create a new author (`false`) or modify an
 * existing one (`true`).
 * @return {Promise<{
 *   author?: {
 *     id: number,
 *     first_name: string,
 *     last_name: string,
 *     full_name: string,
 *   }
 *   errors?: string[]
 * }>}
 */
function onAuthorFormSubmit(e, $modal, isEditing = false) {
  e.preventDefault();
  const $form = $(e.target);
  const $errorContainer = $modal.find(".error-div");
  const data = {};
  $form.serializeArray().forEach(obj => data[obj.name] = obj.value);
  if (isEditing) {
    // add author ID to data
    data["id"] = selectedAuthor.id;
  }
  return new Promise((resolve, reject) => {
    $.post({
      url: window.addEditAuthorUrl,
      headers: {"X-CSRF-Token": data["crsfmiddlewaretoken"]},
      data,
      success: response => resolve(response),
      error: (jqXHR, _status, _err) => reject(`${jqXHR.status} - ${jqXHR.statusText}`),
    });
  })
    .then(response => {
      if (response.errors) {
        // display error messages
        $errorContainer.html("");  // clear previous errors
        response.errors.forEach(errorMsg => $errorContainer.append(`<small class="text-danger">${errorMsg}</small>`));
      }
      return response;
    })
    .catch(err => {
      console.error("Error submitting author form:", err);
      $errorContainer.html(`<small class="text-danger">An unexpected error occurred: ${err}</small>`);
    });
}

/**
 * Sets the name input fields of a author edit field to the given fields.
 * @param $modal JQuery to the modal whose fields should be set.
 * @param firstName Value to set the first name input to.
 * @param lastName Value to set the last name input to.
 */
function setAuthorModalFields($modal, firstName, lastName) {
  $modal.find("#first-name-txt").val(firstName);
  $modal.find("#last-name-txt").val(lastName);
}
