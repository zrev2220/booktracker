"use strict";

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

function setAuthorModalFields($modal, firstName, lastName) {
  $modal.find("#first-name-txt").val(firstName);
  $modal.find("#last-name-txt").val(lastName);
}

function onEditModalWillShow(e) {
  setAuthorModalFields($(e.target), selectedAuthor.firstName, selectedAuthor.lastName);
}

function onEditModalDidHide(e) {
  setAuthorModalFields($(e.target), "", "");
  selectedAuthor = null;
}

function editAuthor(id, firstName, lastName) {
  selectedAuthor = {id, firstName, lastName};
  $("#edit-author-modal").modal();
}

function deleteAuthor(id, firstName, lastName) {
  selectedAuthor = {id, firstName, lastName};
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
