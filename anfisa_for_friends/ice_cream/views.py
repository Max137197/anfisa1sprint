from django.shortcuts import render, get_object_or_404

# Демонстрационные данные мороженого
ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
]

def ice_cream_list(request):
    # Отображаем каталог мороженого
    context = {'ice_cream_list': ice_cream_catalog}
    return render(request, 'ice_cream/list.html', context)

def ice_cream_detail(request, pk):
    # Отображаем подробности выбранного мороженого
    try:
        ice_cream = next(item for item in ice_cream_catalog if item['id'] == pk)
    except StopIteration:
        # Если не найден, возвращаем 404
        from django.http import Http404
        raise Http404("Ice cream not found")
    context = {'ice_cream': ice_cream}
    return render(request, 'ice_cream/detail.html', context)
