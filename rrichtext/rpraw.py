from typing import TYPE_CHECKING

import praw

if TYPE_CHECKING:
    from .document import RichTextContent


def reply(
    instance: "praw.Reddit",
    thing: "praw.models.reddit.mixins.ReplyableMixin",
    body: "RichTextContent",
) -> "praw.models.Comment | praw.models.Message | None":
    """Reply to the object.

    :param body: The RichText content for a comment.

    :returns: A :class:`praw.models.Comment` or :class:`praw.models.Message` object for the newly created
        comment or message or ``None`` if Reddit doesn't provide one.

    :raises: ``prawcore.exceptions.Forbidden`` when attempting to reply to some
        items, such as locked submissions/comments or non-replyable messages.

    A ``None`` value can be returned if the target is a comment or submission in a
    quarantined subreddit and the authenticated user has not opt-ed into viewing the
    content. When this happens the comment will be successfully created on Reddit
    and can be retried by drawing the comment from the user's comment history.

    Example usage:

    .. code-block:: python

        submission = reddit.submission("5or86n")
        rpraw.reply(reddit, submission, RichTextContent([...]))

        comment = reddit.comment("dxolpyc")
        rpraw.reply(reddit, comment, RichTextContent([...]))

    """
    data = {"api_type": "json", "richtext_json": body.to_json(), "thing_id": thing.fullname}
    comments = instance.post(praw.endpoints.API_PATH["comment"], data=data)
    try:
        return comments[0]
    except IndexError:
        return None


def submit(
    instance: "praw.Reddit",
    subreddit: "praw.models.Subreddit",
    title: str,
    selftext: "RichTextContent",
    *,
    collection_id: str | None = None,
    discussion_type: str | None = None,
    draft_id: str | None = None,
    flair_id: str | None = None,
    flair_text: str | None = None,
    nsfw: bool = False,
    resubmit: bool = True,
    send_replies: bool = True,
    spoiler: bool = False,
) -> praw.models.Submission:
    r"""Add a submission to the :class:`.Subreddit`.

    :param title: The title of the submission.
    :param collection_id: The UUID of a :class:`.Collection` to add the
        newly-submitted post to.
    :param discussion_type: Set to ``"CHAT"`` to enable live discussion instead of
        traditional comments (default: ``None``).
    :param draft_id: The ID of a draft to submit.
    :param flair_id: The flair template to select (default: ``None``).
    :param flair_text: If the template's ``flair_text_editable`` value is ``True``,
        this value will set a custom text (default: ``None``). ``flair_id`` is
        required when ``flair_text`` is provided.
    :param nsfw: Whether the submission should be marked NSFW (default: ``False``).
    :param resubmit: When ``False``, an error will occur if the URL has already been
        submitted (default: ``True``).
    :param selftext: The RichText content for a ``text`` submission.
    :param send_replies: When ``True``, messages will be sent to the submission
        author when comments are made to the submission (default: ``True``).
    :param spoiler: Whether the submission should be marked as a spoiler (default:
        ``False``).

    :returns: A :class:`praw.models.Submission` object for the newly created submission.


    .. note::

        To submit a post to a subreddit with the ``"news"`` flair, you can get the
        flair id like this:

        .. code-block::

            choices = list(subreddit.flair.link_templates.user_selectable())
            template_id = next(x for x in choices if x["flair_text"] == "news")["flair_template_id"]
            subreddit.submit("title", flair_id=template_id, selftext=RichTextContent([...]))

    .. seealso::

        - :meth:`praw.models.Subreddit.submit_gallery` to submit more than one image in the
          same post
        - :meth:`praw.models.Subreddit.submit_image` to submit images
        - :meth:`praw.models.Subreddit.submit_poll` to submit polls
        - :meth:`praw.models.Subreddit.submit_video` to submit videos and videogifs

    """

    data = {
        "sr": str(subreddit),
        "resubmit": bool(resubmit),
        "sendreplies": bool(send_replies),
        "title": title,
        "nsfw": bool(nsfw),
        "spoiler": bool(spoiler),
        "validate_on_submit": instance.validate_on_submit,
    }
    for key, value in (
        ("flair_id", flair_id),
        ("flair_text", flair_text),
        ("collection_id", collection_id),
        ("discussion_type", discussion_type),
        ("draft_id", draft_id),
    ):
        if value is not None:
            data[key] = value
    data.update(kind="self")
    data.update(text=selftext.to_json())

    return instance.post(praw.endpoints.API_PATH["submit"], data=data)
