(function()
{
	Sidebar.prototype.addBasicPalette = function()
	{
		var w = 100;
		var h = 100;
		var s = 'strokeWidth=2;whiteSpace=wrap;html=1;shape=mxgraph.basic.';
		var s2 = mxConstants.STYLE_VERTICAL_LABEL_POSITION + '=bottom;' + mxConstants.STYLE_VERTICAL_ALIGN + '=top;html=1;strokeWidth=2;shape=mxgraph.basic.';
		var s3 = mxConstants.STYLE_VERTICAL_LABEL_POSITION + '=bottom;' + mxConstants.STYLE_VERTICAL_ALIGN + '=top;html=1;strokeWidth=2;shape=';
		var gn = 'mxgraph.basic';
		var dt = '';
		
		this.addPaletteFunctions('basic', mxResources.get('basic'), false,
		[
			this.createVertexTemplateEntry('shape=partialRectangle;whiteSpace=wrap;html=1;top=0;bottom=0;fillColor=none;', 120, 60, '', 'Partial Rectangle'),
			this.createVertexTemplateEntry('shape=partialRectangle;whiteSpace=wrap;html=1;right=0;top=0;bottom=0;fillColor=none;routingCenterX=-0.5;', 120, 60, '', 'Partial Rectangle'),
			this.createVertexTemplateEntry('shape=partialRectangle;whiteSpace=wrap;html=1;bottom=0;right=0;fillColor=none;', 120, 60, '', 'Partial Rectangle'),
			this.createVertexTemplateEntry('shape=partialRectangle;whiteSpace=wrap;html=1;top=0;left=0;fillColor=none;', 120, 60, '', 'Partial Rectangle'),
			this.createVertexTemplateEntry(s2 + '4_point_star_2;dx=0.8;', w, h, '', '4 Point Star', null, null, this.getTagsForStencil(gn, '4_point_star', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + '6_point_star', w, h * 0.9, '', '6 Point Star', null, null, this.getTagsForStencil(gn, '6_point_star', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + '8_point_star', w, h, '', '8 Point Star', null, null, this.getTagsForStencil(gn, '8_point_star', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'banner', w, h * 0.5, '', 'Banner', null, null, this.getTagsForStencil(gn, 'banner', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'cloud_callout', w * 0.9, h * 0.6, '', 'Cloud Callout', null, null, this.getTagsForStencil(gn, 'cloud_callout', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'cone', w, h, '', 'Cone', null, null, this.getTagsForStencil(gn, 'cone', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'cone2;dx=0.5;dy=0.9;', w, h, '', 'Cone (adjustable)', null, null, this.getTagsForStencil(gn, 'cone', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'document', w, h, '', 'Document', null, null, this.getTagsForStencil(gn, 'document', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'donut;dx=25;', w, h, '', 'Donut', null, null, this.getTagsForStencil(gn, 'donut', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'drop', w * 0.7, h, '', 'Drop', null, null, this.getTagsForStencil(gn, 'drop', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'flash', w * 0.6, h, '', 'Flash', null, null, this.getTagsForStencil(gn, 'flash', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'half_circle', w, h * 0.5, '', 'Half Circle', null, null, this.getTagsForStencil(gn, 'half_circle', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'heart', w, h, '', 'Heart', null, null, this.getTagsForStencil(gn, 'heart', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'isocube;isoAngle=15;', w, h, '', 'Isometric Cube', null, null, this.getTagsForStencil(gn, 'isometric cube', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'loud_callout', w, h * 0.6, '', 'Loud Callout', null, null, this.getTagsForStencil(gn, 'loud_callout', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'moon', w * 0.75, h, '', 'Moon', null, null, this.getTagsForStencil(gn, 'moon', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'no_symbol', w, h, '', 'No Symbol', null, null, this.getTagsForStencil(gn, 'no_symbol', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'octagon2;align=center;verticalAlign=middle;dx=15;', w, h, '', 'Octagon', null, null, this.getTagsForStencil(gn, 'octagon', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'orthogonal_triangle', w, h * 0.7, '', 'Orthogonal Triangle', null, null, this.getTagsForStencil(gn, 'orthogonal_triangle', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'acute_triangle;dx=0.5;', w, h * 0.7, '', 'Acute Triangle', null, null, this.getTagsForStencil(gn, 'acute_triangle', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'obtuse_triangle;dx=0.25;', w, h * 0.7, '', 'Obtuse Triangle', null, null, this.getTagsForStencil(gn, 'obtuse_triangle', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'oval_callout', w, h * 0.6, '', 'Oval Callout', null, null, this.getTagsForStencil(gn, 'oval_callout', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'pentagon', w, h * 0.9, '', 'Pentagon', null, null, this.getTagsForStencil(gn, 'pentagon', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'pointed_oval', w * 0.5, h, '', 'Pointed Oval', null, null, this.getTagsForStencil(gn, 'pointed oval', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'pyramid;dx1=0.4;dx2=0.6;dy1=0.9;dy2=0.8;', w, h, '', 'Pyramid', null, null, this.getTagsForStencil(gn, 'pyramid', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'diag_snip_rect;dx=6;', w, h * 0.6, '', 'Diagonal Snip Rectangle', null, null, this.getTagsForStencil(gn, 'diag_snip_rect', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'diag_round_rect;dx=6;', w, h * 0.6, '', 'Diagonal Rounded Rectangle', null, null, this.getTagsForStencil(gn, 'diag_round_rect', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'corner_round_rect;dx=6;', w, h * 0.6, '', 'Corner Rounded Rectangle', null, null, this.getTagsForStencil(gn, 'corner_round_rect', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'plaque;dx=6;', w, h * 0.6, '', 'Plaque', null, null, this.getTagsForStencil(gn, 'plaque', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'frame;dx=10;', w, h * 0.6, '', 'Frame', null, null, this.getTagsForStencil(gn, 'frame', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'rounded_frame;dx=10;', w, h * 0.6, '', 'Rounded Frame', null, null, this.getTagsForStencil(gn, 'rounded_frame', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'plaque_frame;dx=10;', w, h * 0.6, '', 'Plaque Frame', null, null, this.getTagsForStencil(gn, 'plaque_frame', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'frame_corner;dx=10;', w, h * 0.6, '', 'Frame Corner', null, null, this.getTagsForStencil(gn, 'frame_corner', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'diag_stripe;dx=10;', w, h * 0.6, '', 'Diagonal Stripe', null, null, this.getTagsForStencil(gn, 'diag_stripe', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'rectCallout;dx=30;dy=15;boundedLbl=1;', w, h * 0.6, '', 'Rectangular Callout', null, null, this.getTagsForStencil(gn, 'rectangular_callout', dt).join(' ')),
			this.createVertexTemplateEntry(s + 'roundRectCallout;dx=30;dy=15;size=5;boundedLbl=1;', w, h * 0.6, '', 'Rounded Rectangular Callout', null, null, this.getTagsForStencil(gn, 'rectangular_callout', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'layered_rect;dx=10;', w, h * 0.6, '', 'Layered Rectangle', null, null, this.getTagsForStencil(gn, 'layered_rect', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'smiley', w, h, '', 'Smiley', null, null, this.getTagsForStencil(gn, 'smiley', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'star', w, h * 0.95, '', 'Star', null, null, this.getTagsForStencil(gn, 'star', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'sun', w, h, '', 'Sun', null, null, this.getTagsForStencil(gn, 'sun', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'tick', w * 0.85, h, '', 'Tick', null, null, this.getTagsForStencil(gn, 'tick', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'wave2;dy=0.3;', w, h * 0.6, '', 'Wave', null, null, this.getTagsForStencil(gn, 'wave', dt).join(' ')),
			this.createVertexTemplateEntry('labelPosition=center;verticalLabelPosition=middle;html=1;strokeWidth=2;shape=mxgraph.basic.button;dx=10;', w, h * 0.6, 'Button', 'Button', null, null, this.getTagsForStencil(gn, 'button', dt).join(' ')),
			this.createVertexTemplateEntry('labelPosition=center;verticalLabelPosition=middle;html=1;strokeWidth=2;shape=mxgraph.basic.shaded_button;dx=10;fillColor=#E6E6E6;strokeColor=none;', w, h * 0.6, 'Button', 'Button (shaded)', null, null, this.getTagsForStencil(gn, 'button', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'x', w, h, '', 'X', null, null, this.getTagsForStencil(gn, 'x', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'pie;startAngle=0.2;endAngle=0.9;', w, h, '', 'Pie', null, null, this.getTagsForStencil(gn, 'pie', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'arc;startAngle=0.3;endAngle=0.1;', w, h, '', 'Arc', null, null, this.getTagsForStencil(gn, 'arc', dt).join(' ')),
			this.createVertexTemplateEntry(s2 + 'partConcEllipse;startAngle=0.25;endAngle=0.1;arcWidth=0.5;', w, h, '', 'Partial Concentric Ellipse', null, null, this.getTagsForStencil(gn, 'partConcEllipse', dt).join(' '))
		]);
	};

})();
