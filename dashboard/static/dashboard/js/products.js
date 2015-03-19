var ProductSKUTable = function(prefix, colCount, extra_attributes, has_errors){
    this.prefix =  prefix;
    this.rowCount = 0;
    this.colCount = colCount;
    this.sku_table = $('#sku_table');
    this.newcol_default_width = 150;
    this.has_errors = has_errors;
    this.extra_attributes = extra_attributes;
}

ProductSKUTable.prototype.Init = function() {

    var that = this;

    $('#sku_col_add_btn').click(function () {
        $('#newSkuColumn').val('');
        $('#newSkuColumnValidation').hide();
        $('#sku_column_add_modal').modal('show');
    })

    $('#addNewAttribute').click(function () {
        var attributeName = $('#newSkuColumn').val();
        if (attributeName == '') {
            $('#newSkuColumn').focus();
            $('#newSkuColumnValidation').show();
            return;
        } else {
            $('#newSkuColumnValidation').hide();
            $('#sku_column_add_modal').modal('hide');
            that.add_new_attribute(attributeName);
        }

    });

    $('#sku_row_add_btn').click(function () {
        that.add_new_row();
    });

    this.rowCount = parseInt($('#id_' + this.prefix + '-TOTAL_FORMS').val()) + 0;

    if (this.rowCount > 1 && !this.has_errors) {
        this.remove_last_row();
    } else if (this.rowCount == 1 && !this.has_errors) {
        this.populate_last_row_skuval();
    }

    this.update_extra_attributes_value();

    for (i = 0; i < this.extra_attributes.length; i++) {
        var attName = this.extra_attributes[i];
        $('#extra_header_remove_' + attName).click(get_remove_attribute_callback(this, attName))
    }
}

function get_remove_attribute_callback(that, attName) {
   return function() {
       that.remove_attribute(attName);
   } 
}

ProductSKUTable.prototype.is_attribute_exist = function(attributeName) {
    var attName = ProductSKUTable.GET_ATTRIBUTE_NAME(attributeName);
    if ($('#id_' + this.prefix + '-0-' + attName).length > 0) return true;
    return false;
}

ProductSKUTable.prototype.remove_attribute = function(attName) {

    if (this.get_active_rows_count() > 1 && this.extra_attributes.length <= 1) {
        alert('At least one custom attribute should exist for multiple rows.');
        return;
    }

    $('#extra_header_' + attName).remove();

    for (var i = 1; i <= this.rowCount; i++) {
        console.log('#extra_attribute_col-' + (i-1) + '-' + attName);
        $('#extra_attribute_col-' + (i-1) + '-' + attName).remove();
    }

    for (var i = 0; i < this.extra_attributes.length; i++) {
        if (this.extra_attributes[i] == attName) {
            this.extra_attributes.splice(i, 1);
            break;
        }
    }

    this.update_extra_attributes_value();

}

ProductSKUTable.prototype.populate_last_row_skuval = function() {

    $('#id_' + this.prefix + '-' + (this.rowCount - 1) + '-code').val(generateRandomSKU());

    $('#id_' + this.prefix + '-' + (this.rowCount - 1) + '-quantity').val(
        $('#id_' + this.prefix + '-' + (this.rowCount - 2) + '-quantity').val()
    );

    $('#id_' + this.prefix + '-' + (this.rowCount - 1) + '-retail_price').val(
        $('#id_' + this.prefix + '-' + (this.rowCount - 2) + '-retail_price').val()
    );

    $('#id_' + this.prefix + '-' + (this.rowCount - 1) + '-sale_price').val(
        $('#id_' + this.prefix + '-' + (this.rowCount - 2) + '-sale_price').val()
    );

    $('#id_' + this.prefix + '-' + (this.rowCount - 1) + '-on_sale').prop('checked',
        $('#id_' + this.prefix + '-' + (this.rowCount - 2) + '-on_sale').prop('checked')
    );

}

ProductSKUTable.prototype.remove_last_row = function() {

    var dataRows = this.sku_table.find('tr');

    var prevRowNum = this.rowCount;

    var last_row = $(dataRows[prevRowNum]);

    if (last_row) last_row.remove();

    this.rowCount = this.rowCount - 1;

    $('#id_' + this.prefix + '-TOTAL_FORMS').val(this.rowCount);

}

ProductSKUTable.prototype.get_active_rows_count = function() {

    var count = 0;

    for (var i = 0; i < this.rowCount; i++) {

        if ($('#id_' + this.prefix + '-' + i + '-DELETE').prop('checked') == false) count++;
    }

    return count;
}

ProductSKUTable.prototype.add_new_row = function(){

    if (this.extra_attributes.length < 1) {
        alert('At least one custom attribute should exist for multiple rows.');
        return;
    }

    var dataRows = this.sku_table.find('tr');

    var prevRowNum = this.rowCount;

    var template_string = $(dataRows[prevRowNum]).html();

    var find = '-' + (prevRowNum - 1) + '-';

    var re = new RegExp(find, 'g');

    template_string = '<tr>' + template_string.replace(re, '-' + prevRowNum + '-') + '</tr>';

    this.sku_table.find('tbody').first().append($(template_string));

    this.rowCount = this.rowCount + 1;

    $('#id_' + this.prefix + '-TOTAL_FORMS').val(this.rowCount);

    this.populate_last_row_skuval();

}

ProductSKUTable.prototype.add_new_attribute = function (attributeName){

    var that = this;

    if (this.is_attribute_exist(attributeName)) {
        alert("Same attribute already exists.");
        return;
    }

    var attName = ProductSKUTable.GET_ATTRIBUTE_NAME(attributeName);

    var newHeaderCol = $('<th width="' + this.newcol_default_width + 'px" id="extra_header_' + attName + '">' + attributeName + '&nbsp;&nbsp;<i class="fa fa-times-circle" style="cursor: pointer" id="extra_header_remove_' + attName + '"></i></th>');

    this.sku_table.find('tr').first().append(newHeaderCol);


    $('#extra_header_remove_'+attName).click(function(){
       that.remove_attribute(attName);
    });

    var dataRows = this.sku_table.find('tr');

    for (var i = 1; i <= this.rowCount; i++) {
        var inputName = this.get_input_name_for_attribute(attName, i);
        var newCol = $(this.get_new_col_cell_html(attName, i));
        $(dataRows[i]).append(newCol);
    }

    this.extra_attributes.push(attName);
    this.update_extra_attributes_value();
}




ProductSKUTable.prototype.update_extra_attributes_value  = function(){
    $('#extra_sku_attributes').val(this.extra_attributes.join(","));
}

ProductSKUTable.prototype.get_new_col_cell_html = function(attName, i){
    var inputName = this.get_input_name_for_attribute(attName, i);
    return '<td id="extra_attribute_col-' + (i-1) + '-' + attName + '"><input id="id_' + inputName + '" name="' + inputName + '" type="text" /></td>';
}

ProductSKUTable.prototype.get_input_name_for_attribute = function(attName, i){
    var inputName = this.prefix + '-' + (i-1) + '-' + attName;
    return inputName;
}



ProductSKUTable.GET_ATTRIBUTE_NAME = function(attributeName){
    return attributeName.toLowerCase().replace(/ /, "_");
    //return attributeName.replace(/([A-Z])/g, function($1){return "_"+$1.toLowerCase();});
}



function initFileReader(){
    if (window.FileReader) {
        $('input[type="file"]').change(function(evt) {
            var reader = new FileReader();
            var imgId = evt.target.id + "-image";
            reader.onload = (function() {
                return function(e) {
                    var imgDiv = $("#"+imgId);
                    imgDiv.children('img').attr('src', e.target.result);
                };
            })();
            reader.readAsDataURL(evt.target.files[0]);
        });
    }
}


function generateRandomSKU(){
    return generateRandomString(4, false) + generateRandomString(6, true);
}


function generateRandomString(length, is_digit){
    var alphaChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var digitChars = "0123456789"
    var randomString = '';
    for (var i = 0; i < length; i++){
        if (is_digit) {
            var rnum = Math.floor(Math.random() * digitChars.length);
            randomString += digitChars.substring(rnum, rnum + 1);
        } else {
            var rnum = Math.floor(Math.random() * alphaChars.length);
            randomString += alphaChars.substring(rnum, rnum + 1);
        }
    }
    return randomString;
}

