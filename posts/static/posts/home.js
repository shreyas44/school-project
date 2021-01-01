$(document).ready(function () {
  $(".post-like-button").click(function () {
    const postId = parseInt($(this).find("input").attr("value"));
    const button = $(this);

    $.ajax({
      type: "POST",
      url: "/toggleLike",
      contentType: "application/json",
      data: JSON.stringify({ post_id: postId }),
      success: (message) => {
        const likeCount = parseInt(
          button.parent().children(".post-like-count").text()
        );
        button
          .parent()
          .children(".post-like-count")
          .text(message === "increase" ? likeCount + 1 : likeCount - 1);
      },
    });
    $(this).toggleClass("fill");
  });

  $(".new-post-body").on("input", function () {
    const text = $(this).text();
    $(this).parent().children("textarea").text(text);
    console.log(text);
  });
});
