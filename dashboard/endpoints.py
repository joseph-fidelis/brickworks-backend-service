from django.db import connections
from django.urls import path
from django.contrib.auth.decorators import login_required
from dashboard import views
from .models import Category, Color, Gear, Minifigure, Part, PartWithColor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from src.ingestion import export_category_to_json, export_color_to_json, export_gears_to_json, export_minifigures_to_json, export_parts_to_json, export_parts_with_colors_to_json


def get_all_category(request):
    try:
        # Get all categories
        categories = Category.objects.using("brick_works").all()

        # Get page number from request
        page_number = request.GET.get("page", 1)

        # Get page size from request
        page_size = request.GET.get("page_size", 20)

        # search query
        search_query = request.GET.get("search", "").strip()

        if search_query:
            categories = categories.filter(
                Q(category_name__icontains=search_query) | Q(category_id__icontains=search_query)
            )

        # Create paginator
        paginator = Paginator(categories, page_size)

        try:
            page_obj = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.page(1)

        # Serialize data
        categories_data = []
        for category in page_obj:
            categories_data.append(
                {
                    "sn": category.id,
                    "name": category.category_name,
                    "id": category.category_id,
                }
            )

        response_data = {
            "success": True,
            "data": categories_data,
            "pagination": {
                "current_page": page_obj.number,
                "total_pages": paginator.num_pages,
                "total_count": paginator.count,
                "page_size": int(page_size),
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e), "data": [], "pagination": {}},
            status=500,
        )

def get_all_color(request):
    try:
        # Get all colors
        colors = Color.objects.using("brick_works").all()

        # Get page number from request
        page_number = request.GET.get("page", 1)

        # Get page size from request
        page_size = request.GET.get("page_size", 20)

        # search query
        search_query = request.GET.get("search", "").strip()

        if search_query:
            colors = colors.filter(
                Q(color_name__icontains=search_query)
                | Q(color_id__icontains=search_query)
                | Q(color_type__icontains=search_query)
            )

        # Create paginator
        paginator = Paginator(colors, page_size)

        try:
            page_obj = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.page(1)

        # Serialize data
        color_data = []
        for color in page_obj:
            color_data.append(
                {
                    "color_id": getattr(color, "color_id", None)
                    or getattr(color, "pk", None),
                    "color_name": color.color_name,
                    "color_type": color.color_type,
                    "color_code": color.color_code,
                }
            )

        response_data = {
            "success": True,
            "data": color_data,
            "pagination": {
                "current_page": page_obj.number,
                "total_pages": paginator.num_pages,
                "total_count": paginator.count,
                "page_size": int(page_size),
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e), "data": [], "pagination": {}},
            status=500,
        )

def get_all_parts(request):
    try:
        # Get all parts
        parts = Part.objects.using("brick_works").all()

        # Get page number from request
        page_number = request.GET.get("page", 1)

        # Get page size from request
        page_size = request.GET.get("page_size", 20)

        # search query
        search_query = request.GET.get("search", "").strip()

        if search_query:
            parts = parts.filter(
                Q(name__icontains=search_query)
                | Q(item_id__icontains=search_query)
                | Q(category__icontains=search_query)
            )

        # Create paginator
        paginator = Paginator(parts, page_size)

        try:
            page_obj = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.page(1)

        # Serialize data
        parts_data = []
        for part in page_obj:
            parts_data.append(
                {
                    "item_id": part.item_id,
                    "item_name": part.name,
                    "category": part.category,
                }
            )

        response_data = {
            "success": True,
            "data": parts_data,
            "pagination": {
                "current_page": page_obj.number,
                "total_pages": paginator.num_pages,
                "total_count": paginator.count,
                "page_size": int(page_size),
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e), "data": [], "pagination": {}},
            status=500,
        )

def get_all_minifigure(request):
    try:
        # Get all minifigures
        minifigures = Minifigure.objects.using("brick_works").all()

        # Get page number from request
        page_number = request.GET.get("page", 1)

        # Get page size from request
        page_size = request.GET.get("page_size", 20)
        try:
            page_size = int(page_size)
        except (TypeError, ValueError):
            page_size = 20

        # search query
        search_query = request.GET.get("search", "").strip()

        if search_query:
            minifigures = minifigures.filter(
                Q(name__icontains=search_query)
                | Q(item_id__icontains=search_query)
                | Q(category__icontains=search_query)
            )

        # Create paginator
        paginator = Paginator(minifigures, page_size)

        try:
            page_obj = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.page(1)

        # Serialize data
        minifigures_data = []
        for mf in page_obj:
            minifigures_data.append(
                {
                    "item_id": mf.item_id,
                    "item_name": mf.name,
                    "category": mf.category,
                }
            )

        response_data = {
            "success": True,
            "data": minifigures_data,
            "pagination": {
                "current_page": page_obj.number,
                "total_pages": paginator.num_pages,
                "total_count": paginator.count,
                "page_size": int(page_size),
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e), "data": [], "pagination": {}},
            status=500,
        )

def get_all_gears(request):
    try:
        # Get all gears
        gears = Gear.objects.using("brick_works").all()

        # Get page number from request
        page_number = request.GET.get("page", 1)

        # Get page size from request
        page_size = request.GET.get("page_size", 20)
        try:
            page_size = int(page_size)
        except (TypeError, ValueError):
            page_size = 20

        # search query
        search_query = request.GET.get("search", "").strip()

        if search_query:
            gears = gears.filter(
                Q(name__icontains=search_query)
                | Q(item_id__icontains=search_query)
                | Q(category__icontains=search_query)
            )

        # Create paginator
        paginator = Paginator(gears, page_size)

        try:
            page_obj = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.page(1)

        # Serialize data
        gears_data = []
        for gear in page_obj:
            gears_data.append(
                {
                    "item_id": gear.item_id,
                    "item_name": gear.name,
                    "category": gear.category,
                }
            )

        response_data = {
            "success": True,
            "data": gears_data,
            "pagination": {
                "current_page": page_obj.number,
                "total_pages": paginator.num_pages,
                "total_count": paginator.count,
                "page_size": int(page_size),
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
        }
        print(response_data)
        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e), "data": [], "pagination": {}},
            status=500,
        )
# parts with colors
def get_all_codes(request):
    try:
        # Get parts with colors
        parts_colors = PartWithColor.objects.using("brick_works").all()

        # Get page number from request
        page_number = request.GET.get("page", 1)

        # Get page size from request
        page_size = request.GET.get("page_size", 20)
        try:
            page_size = int(page_size)
        except (TypeError, ValueError):
            page_size = 20

        # search query
        search_query = request.GET.get("search", "").strip()

        if search_query:
            parts_colors = parts_colors.filter(
                Q(item_id__icontains=search_query)
                | Q(color_name__icontains=search_query)
                | Q(item_type__icontains=search_query)
                | Q(sn__icontains=search_query)
            )

        # Create paginator
        paginator = Paginator(parts_colors, page_size)

        try:
            page_obj = paginator.page(page_number)
        except (PageNotAnInteger, EmptyPage):
            page_obj = paginator.page(1)

        # Serialize data
        parts_colors_data = []
        for pc in page_obj:
            parts_colors_data.append(
                {
                    "s/n": pc.sn,
                    "item_id": pc.item_id,
                    "color_name": pc.color_name,
                    "item_type": pc.item_type,
                }
            )

        response_data = {
            "success": True,
            "data": parts_colors_data,
            "pagination": {
                "current_page": page_obj.number,
                "total_pages": paginator.num_pages,
                "total_count": paginator.count,
                "page_size": int(page_size),
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
        }

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse(
            {"success": False, "error": str(e), "data": [], "pagination": {}},
            status=500,
        )


# ##### Function Calls 

@login_required(login_url='login')
def export_category(request):
    data = export_category_to_json()
    return JsonResponse({'status': 'success', 'data': data})

@login_required(login_url='login')
def export_color(request):
    data = export_color_to_json()
    return JsonResponse({'status': 'success', 'data': data})

@login_required(login_url='login')
def export_parts(request):
    data = export_parts_to_json()
    return JsonResponse({'status': 'success', 'data': data})

@login_required(login_url='login')
def export_minifigure(request):
    data = export_minifigures_to_json()
    return JsonResponse({'status': 'success', 'data': data})

@login_required(login_url='login')
def export_gear(request):
    data = export_gears_to_json()
    return JsonResponse({'status': 'success', 'data': data})

@login_required(login_url='login')
def export_parts_with_color(request):
    data = export_parts_with_colors_to_json()
    return JsonResponse({'status': 'success', 'data': data})

urlpatterns = [
    path("category/", get_all_category, name="get_all_category"),
    path("export/category/",export_category,name="export_category"),
    path("export/color/",export_color,name="export_color"),
    path("export/parts/",export_parts,name="export_parts"),
    path("export/minifigure/",export_minifigure,name="export_minifigure"),
    path("export/gears/",export_gear,name="export_gears"),
    path("export/codes/",export_parts_with_color,name="export_codes"),
    path("color/", get_all_color, name="get_all_color"),
    path("part/", get_all_parts, name="get_all_part"),
    path("minifigure/", get_all_minifigure, name="get_all_minifigure"),
    path("gear/", get_all_gears, name="get_all_gear"),
    path("code/", get_all_codes, name="get_all_code"),
]
