"use strict";

$(() => {
  // stagger multiple alerts slightly
  let margin = 0;
  $("#message-alerts .alert").each((i, e) => {
    $(e).css("margin-top", margin);
    // stop increasing margin after 5
    if (i < 5) {
      margin += 5;
    }
  });
});
