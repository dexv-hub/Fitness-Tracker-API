def filter_and_sort_queryset(queryset, request, date_field="date", sort_fields=None):
    date = request.GET.get("date")
    if date:
        queryset = queryset.filter(**{date_field: date})

    date_from = request.GET.get("from")
    date_to = request.GET.get("to")
    if date_from and date_to:
        queryset = queryset.filter(**{f"{date_field}__gte": date_from,
                                     f"{date_field}__lte": date_to})

    sort = request.GET.get("sort")
    if sort and sort_fields and sort in sort_fields:
        queryset = queryset.order_by(sort_fields[sort])

    return queryset
