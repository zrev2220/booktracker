"use strict";

/**
 * Object containing info about the currently-selected author.
 * @type {{
 *   id: number,
 *   firstName: string,
 *   lastName: string,
 *   fullName: string,
 * } | null}
 */
let selectedAuthor = null;

$(() => {
  const $addAuthorModal = $("#add-author-modal");
  const $editAuthorModal = $("#edit-author-modal");

  $addAuthorModal.find("form").on("submit",
      e => afterAddAuthorSubmit($addAuthorModal, onAuthorFormSubmit(e, $addAuthorModal))
  );
  $editAuthorModal
    .on("show.bs.modal", e => onEditModalWillShow(e))
    .on("hidden.bs.modal", e => onEditModalDidHide(e));
  $editAuthorModal.find("form").on("submit", e =>
    afterEditAuthorSubmit($editAuthorModal, onAuthorFormSubmit(e, $editAuthorModal, true))
  );
});

/**
 * Handler for when the edit author modal is about to show.
 *
 * Sets the form fields using info from the {@link selectedAuthor} object.
 * @param e `hidden.bs.modal` event object.
 */
function onEditModalWillShow(e) {
  setAuthorModalFields($(e.target), selectedAuthor.firstName, selectedAuthor.lastName);
}

/**
 * Handler for after the edit author modal is hidden.
 *
 * Clears the form fields and the {@link selectedAuthor} object.
 * @param e `hidden.bs.modal` event object.
 */
function onEditModalDidHide(e) {
  setAuthorModalFields($(e.target), "", "");
  selectedAuthor = null;
}

/**
 * Opens a modal for editing an author entry.
 * @param id ID of author.
 * @param firstName First name of author.
 * @param lastName Last name of author.
 * @param fullName Full name of author.
 */
function editAuthor(id, firstName, lastName, fullName) {
  selectedAuthor = {id, firstName, lastName, fullName};
  $("#edit-author-modal").modal();
}

/**
 * Opens a modal confirming author deletion.
 * @param id ID of author.
 * @param firstName First name of author.
 * @param lastName Last name of author.
 * @param fullName Full name of author.
 */
function deleteAuthor(id, firstName, lastName, fullName) {
  selectedAuthor = {id, firstName, lastName, fullName};
  $("#delete-author-modal").modal();
}

/**
 * Handler after receiving a response from an add author request.
 * @param $modal JQuery of modal responsible for the submission.
 * @param submission {Promise<{
 *   author?: {
 *     id: number,
 *     first_name: string,
 *     last_name: string,
 *     full_name: string,
 *   }
 *   errors?: string[]
 * }>} Promise for submission, resolves after request finishes.
 */
function afterAddAuthorSubmit($modal, submission) {
  submission.then(response => {
    if (response.errors) {
      return;
    }
    // refresh page
    location.reload();
  });
}

/**
 * Handler after receiving a response from an edit author request.
 * @param $modal JQuery of modal responsible for the submission.
 * @param submission {Promise<{
 *   author?: {
 *     id: number,
 *     first_name: string,
 *     last_name: string,
 *     full_name: string,
 *   }
 *   errors?: string[]
 * }>} Promise for submission, resolves after request finishes.
 */
function afterEditAuthorSubmit($modal, submission) {
  submission.then(response => {
    if (response.errors) {
      return;
    }
    // update entry in list
    const {id, first_name, last_name} = response.author;
    const $entry = $(`#author-item-${id}`);
    $entry.find(".first-name").text(first_name);
    $entry.find(".last-name").text(last_name);
    // dismiss modal
    $modal.modal("hide");
  });
}
