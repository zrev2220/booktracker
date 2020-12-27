"use strict";

// declare jQuery vars
let $addAuthorBtn, $addAuthorModal, $addCategoryBtn;

$(() => {
  // initialize jQuery vars
  // note: window.authorId and window.categoryId are set in inline script in book_form.html
  $addAuthorBtn = $(`#add-entry-${window.authorId}`);
  $addAuthorModal = $("#add-author-modal");
  $addCategoryBtn = $(`#add-entry-${window.categoryId}`);

  // register event handlers
  $addAuthorModal.find("form").on("submit",
    e => afterAuthorSubmit($addAuthorModal, onAuthorFormSubmit(e, $addAuthorModal))
  );
  // author form dismiss handler; clear inputs after dismissal
  $addAuthorModal.on("hide.bs.modal", e => $(e.target).find(".modal-body input").val(""));
});

/**
 * Handler after receiving a response from the add/edit author request.
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
function afterAuthorSubmit($modal, submission) {
  submission.then(response => {
    if (response.errors) {
      return;
    }
    // add author to list
    const {id, full_name} = response.author;
    const $authorSelect = $("#" + window.authorId);
    $authorSelect.prepend(`<option value="${id}">${full_name}</option>`);
    // scroll new author into view
    // see https://stackoverflow.com/a/7206039/6548555
    $authorSelect.scrollTop($authorSelect.find(`option[value=${id}]`).offset().top - $authorSelect.offset().top);
    // dismiss modal
    $modal.modal("hide");
  });
}
