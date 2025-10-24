# apps/portal/templates/templatetags/portal_tags.py
from django import template

register = template.Library()

@register.inclusion_tag('portal/components/modal_select_entity.html', takes_context=True)
def render_entity_modal_select(context, field_name, search_url, modal_id, label, css_class='col-12 form-group'):
    """
    Renderiza um componente modal para seleção de Entidade.

    Uso:
        {% render_entity_modal_select field_name search_url modal_id label [css_class] %}

    Argumentos:
    - **field_name**: O nome do campo de formulário.
    - **search_url**: A URL para realizar a busca das entidades.
    - **modal_id**: O ID HTML do modal.
    - **label**: O texto do label associado ao campo.
    - **css_class** (opcional): Classes CSS para o contêiner principal. Padrão é 'col-12 form-group'.

    Exemplo:
        {% render_entity_modal_select 'entidade' '/buscar/entidades/' 'entityModal' 'Selecione a Entidade' 'col-12 form-group' %}
    """
    return {
        'field_name': field_name,
        'search_url': search_url,
        'modal_id': modal_id,
        'label': label,
        'css_class': css_class,
    }


@register.inclusion_tag('portal/components/modal_select_enjoyer.html', takes_context=True)
def render_enjoyer_selector(context, field_name, search_url, modal_id, modal_title, prefix, css_class='col-12 form-group', button_class="btn btn-primary", button_text="Selecionar"):
    """
    Renderiza um componente modal para seleção de Enjoyer.

    Uso:
        {% render_enjoyer_selector field_name search_url modal_id modal_title prefix [css_class] [button_class] [button_text] %}

    Argumentos:
    - **field_name**: O nome do campo de formulário.
    - **search_url**: A URL para realizar a busca dos enjoyers.
    - **modal_id**: O ID HTML do modal.
    - **modal_title**: O título exibido no modal.
    - **prefix**: Prefixo para diferenciar elementos HTML em caso de múltiplos modais.
    - **css_class** (opcional): Classes CSS para o contêiner principal. Padrão é 'col-12 form-group'.
    - **button_class** (opcional): Classes CSS para o botão de seleção. Padrão é 'btn btn-primary'.
    - **button_text** (opcional): Texto exibido no botão de seleção. Padrão é 'Selecionar'.

    Exemplo:
        {% render_enjoyer_selector 'usuario' '/buscar/usuarios/' 'enjoyerModal' 'Selecione o Usuário' 'user' 'btn btn-success' 'Escolher' 'col-12 form-group' %}
    """
    return {
        'field_name': field_name,
        'search_url': search_url,
        'modal_id': modal_id,
        'modal_title': modal_title,
        'prefix': prefix,
        'css_class': css_class,
        'button_class': button_class,
        'button_text': button_text,
    }
