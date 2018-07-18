{% extends 'display_priority.tpl' %}


{% block in_prompt %}
{% endblock in_prompt %}

{% block output_prompt %}
{%- endblock output_prompt %}

{% block input %}
```
{%- if 'magics_language' in cell.metadata  -%}
    {{ cell.metadata.magics_language}}
{%- elif 'name' in nb.metadata.get('language_info', {}) -%}
    {{ nb.metadata.language_info.name }}
{%- endif %}
{{ cell.source}}
```
{% endblock input %}

{% block error %}
{{ super() }}
{% endblock error %}

{% block traceback_line %}
{{ line | indent | strip_ansi }}
{% endblock traceback_line %}

{% block execute_result %}

{% block data_priority scoped %}
{{ super() }}
{% endblock %}
{% endblock execute_result %}

{% block stream %}
{{ '{%' }} raw {{ '%}' }}
<div class="output">
输出(stream):<br>
{{ output.text   | replace('\n', '\n<br />') | indent }}
</div>
{{ '{%' }} endraw {{ '%}' }}
{% endblock stream %}

{% block data_svg %}
![svg]({{ output.metadata.filenames['image/svg+xml'] | path2url }})
{% endblock data_svg %}

{% block data_png %}
![png]({{ output.metadata.filenames['image/png'] | path2url }})
{% endblock data_png %}

{% block data_jpg %}
![jpeg]({{ output.metadata.filenames['image/jpeg'] | path2url }})
{% endblock data_jpg %}

{% block data_latex %}
{{ '{%' }} raw {{ '%}' }}
<div class="output">
输出(text):<br>
{{ output.data['text/latex']   | replace('\n', '\n<br />') | indent}}
</div>
{{ '{%' }} endraw {{ '%}' }}
{% endblock data_latex %}

{% block data_html scoped %}
{{ '{%' }} raw {{ '%}' }}
<div class="output">
输出(html):<br>
{{ output.data['text/html'] }}
</div>
{{ '{%' }} endraw {{ '%}' }}
{% endblock data_html %}

{% block data_markdown scoped %}
{{ output.data['text/markdown'] }}
{% endblock data_markdown %}

{% block data_text scoped %}
{{ '{%' }} raw {{ '%}' }}
<div class="output">
输出(plain):<br/>
{% autoescape false %}
{{ output.data['text/plain']  | replace('\n', '\n<br />') | indent }}
{% endautoescape %}
</div>
{{ '{%' }} endraw {{ '%}' }}
{% endblock data_text %}
{% block markdowncell scoped %}
{{ cell.source | mathjax }}
{% endblock markdowncell %}

{% block unknowncell scoped %}
unknown type  {{ cell.type }}
{% endblock unknowncell %}