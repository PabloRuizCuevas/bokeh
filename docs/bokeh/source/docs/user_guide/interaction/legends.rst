.. _ug_interaction_legends:

Interactive legends
-------------------

:ref:`ug_basic_annotations_legends` added to Bokeh plots can be made interactive
so that clicking or tapping on the legend entries will hide or mute the
corresponding glyph in a plot. These modes are activated by setting the
``click_policy`` property on a :class:`~bokeh.models.annotation.Legend` to
either ``"hide"`` or ``"mute"``.

.. note::
    Interactive legends only work on "per-glyph" legends. Grouped legends
    do not yet support the features described below.

Hiding glyphs
~~~~~~~~~~~~~

Sometimes it is desirable to be able to hide glyphs by clicking on an entry
in a ``Legend``. In Bokeh this can be accomplished by setting the legend
``click_policy`` property to ``"hide"`` as shown in the example below:

.. bokeh-plot:: __REPO__/examples/interaction/legends/legend_hide.py
    :source-position: above

Muting glyphs
~~~~~~~~~~~~~

Other times it is preferable for legend interaction to mute a glyph, instead
of hiding it entirely. In this case, set ``click_policy`` property to
``"mute"``. Additionally, the visual properties of a "muted glyph" also
need to be specified. In general, this is done in exactly the same way as for
:ref:`ug_basic_styling_selected_unselected_glyphs` or
:ref:`ug_basic_styling_hover_inspections`. In the example below,
``muted_alpha=0.2`` and ``muted_color=color`` are passed to ``circle`` to
specify that muted lines should be drawn with a low alpha muted glyph.

.. bokeh-plot:: __REPO__/examples/interaction/legends/legend_mute.py
    :source-position: above
