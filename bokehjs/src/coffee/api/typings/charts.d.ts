declare namespace Bokeh.Charts {
    interface IPieOpts {
        inner_radius?: number;
        outer_radius?: number;
        start_angle?: number;
        end_angle?: number;
        center?: [number, number];
        treshold?: number;
        palette?: Palette | Array<Color>;
        slice_labels?: "labels" | "values" | "percentages";
    }

    function pie(data: {labels: Array<string>, values: Array<number>}, opts?: IPieOpts): Plot;

    interface IBarOpts {
        stacked?: boolean;
        orientation?: "horizontal" | "vertical";
        bar_width?: number;
    }

    function bar(data: Array<Array<string | number>>, opts?: IBarOpts): Plot;
}
