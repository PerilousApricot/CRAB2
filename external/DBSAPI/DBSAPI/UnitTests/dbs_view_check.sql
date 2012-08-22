set serveroutput on size 100000
DECLARE 
   CURSOR cur_view IS SELECT view_name FROM user_views;
   v_view user_views.view_name%TYPE;
BEGIN
   -- Views
   OPEN cur_view;
   LOOP
      FETCH cur_view INTO v_view;
      EXIT WHEN cur_view%NOTFOUND;
      dbms_output.put_line ('select count(*) into l_count from '|| v_view || ';');
   END LOOP;    
   CLOSE cur_view;
END;
/
